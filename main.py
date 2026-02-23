from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.login_screen import LoginScreen


class WindowManager(ScreenManager):
    pass


class WanabeSpotifyApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm


if __name__ == "__main__":
    WanabeSpotifyApp().run()