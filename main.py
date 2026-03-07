from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from data_store import clear_current_user
from screen.login_screen import LoginScreen
from screen.register_screen import RegisterScreen
from screen.home_screen import HomeScreen, SongCard, RecommendCard
from screen.player_screen import PlayerScreen
from screen.search_screen import SearchScreen
from screen.favorite_screen import FavoriteScreen
from screen.profile_screen import ProfileScreen
from screen.add_song_screen import AddSongScreen

APP_VERSION = "1.0.0"


class RootWidget(ScreenManager):
    def logout(self):
        clear_current_user()
        self.current = "login"


class WanabeSpotifyApp(MDApp):
    def build(self):
        self.title = f"WanabeSpotify v{APP_VERSION}"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.accent_palette = "Purple"
        return Builder.load_file("wanabe_spotify.kv")


if __name__ == "__main__":
    WanabeSpotifyApp().run()