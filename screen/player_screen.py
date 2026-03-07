import os

from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivymd.uix.screen import MDScreen

from data_store import toggle_favorite, is_favorite, get_song_file, get_song_lyrics


class PlayerScreen(MDScreen):
    song_title = StringProperty("No Song")
    song_artist = StringProperty("Unknown Artist")
    song_duration = StringProperty("0:00")
    song_lyrics = StringProperty("No lyrics available for this song yet.")

    current_time = StringProperty("0:00")
    progress = NumericProperty(0)
    playback_status = StringProperty("")

    is_playing = BooleanProperty(False)
    is_favorite_song = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_sound = None
        Clock.schedule_interval(self.update_progress, 0.5)

    def load_song(self, title, artist, duration):
        self.stop_current_sound()

        self.song_title = title
        self.song_artist = artist
        self.song_duration = duration
        self.song_lyrics = get_song_lyrics(title, artist)
        self.current_time = "0:00"
        self.progress = 0
        self.is_playing = False
        self.playback_status = ""
        self.is_favorite_song = is_favorite(title, artist)

        song_file = get_song_file(title, artist)

        if song_file:
            self.current_sound = SoundLoader.load(song_file)
            if not self.current_sound and song_file.lower().endswith(".mp4"):
                self.current_sound = self._load_mp4_with_ffpyplayer(song_file)

            if not self.current_sound:
                ext = os.path.splitext(song_file)[1].lower()
                if ext == ".mp4":
                    self.playback_status = "Cannot play .mp4 on this device. Install ffpyplayer and restart app."
                else:
                    self.playback_status = f"Cannot play this file: {os.path.basename(song_file)}"
        else:
            self.current_sound = None
            self.playback_status = f"Audio file not found for: {title}"

    def toggle_play_pause(self):

        if not self.current_sound:
            self.playback_status = "No audio loaded"
            return

        if self.is_playing:
            self.current_sound.stop()
            self.is_playing = False
            self.progress = 0
            self.current_time = "0:00"
            self.playback_status = ""
        else:
            self.current_sound.play()
            self.is_playing = True
            self.playback_status = ""

    def on_play(self):
        self.toggle_play_pause()

    def on_pause(self):
        if self.current_sound and self.is_playing:
            self.current_sound.stop()

        self.is_playing = False
        self.progress = 0
        self.current_time = "0:00"

    def on_prev(self):
        print("Previous song")

    def on_next(self):
        print("Next song")

    def on_seek(self, value):

        if self.current_sound and hasattr(self.current_sound, "seek") and self.current_sound.length:
            try:
                seek_time = (value / 100) * self.current_sound.length
                self.current_sound.seek(seek_time)
                self.current_time = self.format_time(seek_time)
            except Exception as e:
                print(f"Seek not supported: {e}")

    def toggle_favorite_song(self):

        self.is_favorite_song = toggle_favorite(
            self.song_title,
            self.song_artist,
            self.song_duration
        )

    def back_home(self):
        self.manager.current = "home"

    def stop_current_sound(self):

        if self.current_sound:
            try:
                self.current_sound.stop()
            except Exception:
                pass

        self.is_playing = False

    def update_progress(self, dt):

        if self.current_sound and self.is_playing and self.current_sound.length:

            pos = self.current_sound.get_pos()

            if pos is not None and pos >= 0:
                self.progress = min(100, (pos / self.current_sound.length) * 100)
                self.current_time = self.format_time(pos)

    def format_time(self, seconds):

        seconds = int(seconds)
        minutes = seconds // 60
        remain = seconds % 60

        return f"{minutes}:{remain:02d}"

    def _load_mp4_with_ffpyplayer(self, song_file):
        try:
            from ffpyplayer.player import MediaPlayer
        except Exception:
            return None

        if not os.path.exists(song_file):
            return None

        try:
            return _FFPyPlayerAudio(song_file, MediaPlayer)
        except Exception:
            return None


class _FFPyPlayerAudio:
    def __init__(self, song_file, media_player_cls):
        self._player = media_player_cls(song_file, ff_opts={"paused": True, "vn": True})
        self._length = 0.0

    @property
    def length(self):
        if self._length:
            return self._length
        try:
            metadata = self._player.get_metadata() or {}
            self._length = float(metadata.get("duration") or 0.0)
        except Exception:
            self._length = 0.0
        return self._length

    def play(self):
        self._player.set_pause(False)

    def stop(self):
        self._player.set_pause(True)
        try:
            self.seek(0)
        except Exception:
            pass

    def seek(self, seconds):
        self._player.seek(max(0.0, float(seconds)), relative=False)

    def get_pos(self):
        pts = self._player.get_pts()
        if pts is None:
            return 0
        return max(0.0, float(pts))