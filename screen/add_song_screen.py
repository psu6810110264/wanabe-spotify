import os
import tkinter as tk
from tkinter import filedialog

from kivy.core.audio import SoundLoader
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from data_store import add_custom_song, get_custom_songs, get_current_user_role
from screen.home_screen import SongCard


class AddSongScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_cover_path = ""
        self.selected_audio_path = ""
        self.selected_duration = ""

    def on_pre_enter(self, *args):
        self.refresh_song_list()
        return super().on_pre_enter(*args)

    def go_home(self):
        self.manager.current = "home"

    def on_add_song(self):
        if get_current_user_role() != "artist":
            self.ids.add_msg.text = "Only Artist accounts can create songs."
            return

        title = self.ids.new_song_title.text.strip()
        artist = self.ids.new_song_artist.text.strip()
        duration = self.selected_duration
        lyrics = self.ids.new_song_lyrics.text.strip()
        category = self.ids.new_song_category.text.strip()
        album = self.ids.new_song_album.text.strip()

        if not title:
            self.ids.add_msg.text = "Please enter song title."
            return

        if not artist:
            self.ids.add_msg.text = "Please enter artist name."
            return

        if not duration:
            self.ids.add_msg.text = "Please upload audio file to detect duration."
            return

        if category == "Select category":
            self.ids.add_msg.text = "Please select a song category."
            return

        if album == "Select album":
            self.ids.add_msg.text = "Please select an album."
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
            category,
            album,
            self.selected_cover_path,
            self.selected_audio_path,
            lyrics,
        )
        self.ids.add_msg.text = message

        if success:
            self.ids.new_song_title.text = ""
            self.ids.new_song_artist.text = ""
            self.ids.new_song_lyrics.text = ""
            self.ids.new_song_category.text = "Select category"
            self.ids.new_song_album.text = "Select album"
            self.selected_cover_path = ""
            self.selected_audio_path = ""
            self.selected_duration = ""
            self.ids.cover_path_label.text = "No image selected"
            self.ids.audio_path_label.text = "No audio selected"
            self.ids.duration_value_label.text = "--:--"
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
            ("Audio Files", "*.mp3 *.wav *.ogg *.mp4"),
            ("All Files", "*.*"),
        ])
        if not path:
            return

        if not path.lower().endswith((".mp3", ".wav", ".ogg", ".mp4")):
            self.ids.add_msg.text = "Audio file must be mp3/wav/ogg/mp4."
            return

        self.selected_audio_path = path
        self.ids.audio_path_label.text = os.path.basename(path)
        duration_seconds = self._detect_audio_duration(path)
        if duration_seconds is None:
            self.selected_duration = ""
            self.ids.duration_value_label.text = "--:--"
            self.ids.add_msg.text = "Cannot read duration from this audio file."
            return

        self.selected_duration = self._format_duration(duration_seconds)
        self.ids.duration_value_label.text = self.selected_duration
        self.ids.add_msg.text = ""

    def _detect_audio_duration(self, path):
        sound = None
        try:
            sound = SoundLoader.load(path)
            if sound and getattr(sound, "length", 0):
                length = float(sound.length)
                if length > 0:
                    return length
        except Exception:
            pass
        finally:
            if sound:
                try:
                    sound.stop()
                except Exception:
                    pass

        try:
            from ffpyplayer.player import MediaPlayer
        except Exception:
            return None

        player = None
        try:
            player = MediaPlayer(path, ff_opts={"paused": True, "vn": True})
            metadata = player.get_metadata() or {}
            length = float(metadata.get("duration") or 0)
            if length > 0:
                return length
        except Exception:
            return None
        finally:
            if player and hasattr(player, "close_player"):
                try:
                    player.close_player()
                except Exception:
                    pass

        return None

    def _format_duration(self, seconds):
        total = int(round(seconds))
        minutes = total // 60
        remain = total % 60
        return f"{minutes}:{remain:02d}"

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
                artist=f"{item['artist']} - {item.get('category', 'Other')} | {item.get('album', 'Singles')}",
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
