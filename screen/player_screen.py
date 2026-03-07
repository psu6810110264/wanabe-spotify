from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty


def _sec_to_mmss(total_seconds):
    total_seconds = max(0, int(total_seconds))
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"


def _mmss_to_sec(value):
    try:
        minute_str, second_str = value.split(":", 1)
        return int(minute_str) * 60 + int(second_str)
    except (ValueError, AttributeError):
        return 0

class PlayerScreen(Screen):
    song_title = StringProperty("No Song Selected")
    song_artist = StringProperty("Unknown Artist")
    song_duration = StringProperty("0:00")
    current_time = StringProperty("0:00")
    progress = NumericProperty(0)
    is_playing = BooleanProperty(False)

    def load_song(self, title, artist, duration):
        self.song_title = title
        self.song_artist = artist
        self.song_duration = duration
        self.current_time = "0:00"
        self.progress = 0
        self.is_playing = True

    def back_home(self):
        """กลับไปหน้า Home"""
        print("[Callback] back_home")
        self.manager.current = 'home'

    def toggle_play_pause(self):
        """สลับสถานะเล่น/หยุดชั่วคราว"""
        self.is_playing = not self.is_playing
        status = "Playing" if self.is_playing else "Paused"
        print(f"[Callback] toggle_play_pause -> {status}")

    def on_next(self):
        """ตัวอย่าง callback ปุ่มเพลงถัดไป"""
        print("[Callback] on_next -> Next track")

    def on_prev(self):
        """ตัวอย่าง callback ปุ่มเพลงก่อนหน้า"""
        print("[Callback] on_prev -> Previous track")

    def on_seek(self, value):
        """อัปเดตเวลาเมื่อเลื่อนแถบความคืบหน้า"""
        self.progress = value
        total_sec = _mmss_to_sec(self.song_duration)
        self.current_time = _sec_to_mmss(total_sec * (value / 100.0))