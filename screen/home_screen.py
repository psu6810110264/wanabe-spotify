# screens/home_screen.py
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def open_player(self, song_id):
        """
        Callback: เปิดหน้า Player เมื่อเลือกเพลง
        """
        print(f"[Callback] open_player triggered with Song ID: {song_id}")
        
        # เปลี่ยนหน้าไปยัง player_screen
        # (สมมติว่าชื่อ screen ใน ScreenManager คือ 'player')
        self.manager.current = 'player'