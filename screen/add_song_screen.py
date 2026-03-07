import re
import os
import tkinter as tk
from tkinter import filedialog

from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from data_store import add_custom_song, get_custom_songs
from screen.home_screen import SongCard


class AddSongScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_cover_path = ""
        self.selected_audio_path = ""

    def on_pre_enter(self, *args):
        self.refresh_song_list()
        return super().on_pre_enter(*args)

    def go_home(self):
        self.manager.current = "home"

    def on_add_song(self):
        title = self.ids.new_song_title.text.strip()
        artist = self.ids.new_song_artist.text.strip()
        duration = self.ids.new_song_duration.text.strip()

        if not title:
            self.ids.add_msg.text = "Please enter song title."
            return

        if not artist:
            self.ids.add_msg.text = "Please enter artist name."
            return

        if not re.fullmatch(r"\d{1,2}:\d{2}", duration):
            self.ids.add_msg.text = "Duration format must be m:ss or mm:ss."
            return

        if not self.selected_cover_path:
            self.ids.add_msg.text = "Please upload cover image."
            return

        if not self.selected_audio_path:
            self.ids.add_msg.text = "Please upload audio file."
            return

        success, message = add_custom_song(
            title,
            artist,
            duration,
            self.selected_cover_path,
            self.selected_audio_path,
        )
        self.ids.add_msg.text = message

        if success:
            self.ids.new_song_title.text = ""
            self.ids.new_song_artist.text = ""
            self.ids.new_song_duration.text = ""
            self.selected_cover_path = ""
            self.selected_audio_path = ""
            self.ids.cover_path_label.text = "No image selected"
            self.ids.audio_path_label.text = "No audio selected"
            self.refresh_song_list()

    def pick_cover_image(self):
        path = self._pick_file([
            ("Image Files", "*.png *.jpg *.jpeg *.webp"),
            ("All Files", "*.*"),
        ])
        if not path:
            return

        if not path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            self.ids.add_msg.text = "Cover image must be png/jpg/jpeg/webp."
            return

        self.selected_cover_path = path
        self.ids.cover_path_label.text = os.path.basename(path)
        self.ids.add_msg.text = ""

    def pick_audio_file(self):
        path = self._pick_file([
            ("Audio Files", "*.mp3 *.wav *.ogg"),
            ("All Files", "*.*"),
        ])
        if not path:
            return

        if not path.lower().endswith((".mp3", ".wav", ".ogg")):
            self.ids.add_msg.text = "Audio file must be mp3/wav/ogg."
            return

        self.selected_audio_path = path
        self.ids.audio_path_label.text = os.path.basename(path)
        self.ids.add_msg.text = ""

    def _pick_file(self, file_types):
        try:
            root = tk.Tk()
            root.withdraw()
            root.attributes("-topmost", True)
        except Exception:
            self.ids.add_msg.text = "Cannot open file picker on this environment."
            return ""
        try:
            return filedialog.askopenfilename(filetypes=file_types)
        finally:
            root.destroy()

    def refresh_song_list(self):
        container = self.ids.add_song_list
        container.clear_widgets()

        songs = get_custom_songs()
        if not songs:
            container.add_widget(
                MDLabel(
                    text="No added songs yet",
                    halign="center",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    size_hint_y=None,
                    height=50,
                )
            )
            return

        for index, item in enumerate(songs, start=1):
            card = SongCard(
                title=item["title"],
                artist=item["artist"],
                rank=f"{index:02d}",
                duration=item["duration"],
                image_icon="playlist-plus",
            )
            card.bind(
                on_release=lambda instance, t=item["title"], a=item["artist"], d=item["duration"]: self.open_player(t, a, d)
            )
            container.add_widget(card)

    def open_player(self, title, artist, duration):
        player = self.manager.get_screen("player")
        player.load_song(title, artist, duration)
        self.manager.current = "player"
