from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen

# โหลด rules ของ kv (ไม่มี root)
Builder.load_file("wanabe_spotify.kv")


class WanabeSpotifyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.current = "login"   # ชัวร์ว่ามีจริง
        return sm


if __name__ == "__main__":
    WanabeSpotifyApp().run()