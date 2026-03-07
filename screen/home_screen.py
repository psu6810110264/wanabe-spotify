# screens/home_screen.py
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def open_player(self, title, artist, duration):
        """เปิดหน้า Player พร้อมข้อมูลเพลงที่เลือก"""
        print(f"[Callback] open_player -> {title} / {artist}")

        player_screen = self.manager.get_screen('player')
        player_screen.load_song(title=title, artist=artist, duration=duration)
        self.manager.current = 'player'