# screens/player_screen.py
from kivy.uix.screenmanager import Screen

class PlayerScreen(Screen):
    def back_home(self):
        """Callback: กลับไปหน้า Home"""
        print("[Callback] back_home triggered")
        self.manager.current = 'home'

    def on_play(self):
        """Callback: ปุ่ม Play"""
        print("[Callback] on_play triggered -> Playing music...")

    def on_pause(self):
        """Callback: ปุ่ม Pause"""
        print("[Callback] on_pause triggered -> Music paused.")

    def on_next(self):
        """Callback: ปุ่ม Next"""
        print("[Callback] on_next triggered -> Skipping to next song.")

    def on_prev(self):
        """Callback: ปุ่ม Prev"""
        print("[Callback] on_prev triggered -> Going to previous song.")