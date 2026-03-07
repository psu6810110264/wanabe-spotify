from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screen.login_screen import LoginScreen
from screen.home_screen import HomeScreen
from screen.player_screen import PlayerScreen
from screen.search_screen import SearchScreen
from screen.favorite_screen import FavoriteScreen


class RootWidget(ScreenManager):

    def logout(self):
        print("[Callback] logout triggered")
        self.current = "login"


class WanabeSpotifyApp(App):
    def build(self):
        return Builder.load_file("wanabe_spotify.kv")


if __name__ == "__main__":
    WanabeSpotifyApp().run()