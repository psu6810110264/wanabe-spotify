# main.py
from kivy.app import App
from kivy.lang import Builder
from screen.home_screen import HomeScreen
from screen.player_screen import PlayerScreen

# โหลดไฟล์ .kv
# (ถ้าไฟล์ kv ชื่อเดียวกับ App class เช่น MiniSpotifyApp -> mini_spotify.kv มันจะโหลดให้อัตโนมัติ
# แต่เพื่อความชัวร์เราโหลดเองเลยก็ได้)
# Builder.load_file('mini_spotify.kv') 

class MiniSpotifyApp(App):
    def build(self):
        # ตัว ScreenManager ถูกกำหนดไว้ในไฟล์ .kv แล้ว
        return Builder.load_file('mini_spotify.kv')

if __name__ == '__main__':
    MiniSpotifyApp().run()