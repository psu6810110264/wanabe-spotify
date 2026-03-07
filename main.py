from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from screen.login_screen import LoginScreen
from screen.home_screen import HomeScreen
from screen.player_screen import PlayerScreen


class SearchScreen(Screen):
    pass


class FavoriteScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class WanabeSpotifyApp(App):
    def build(self):
        return Builder.load_file("wanabe_spotify.kv")


if __name__ == "__main__":
    WanabeSpotifyApp().run()