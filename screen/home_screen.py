from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen


class SongCard(MDCard):
    title = StringProperty("")
    artist = StringProperty("")
    rank = StringProperty("")
    duration = StringProperty("")
    image_icon = StringProperty("music")


class RecommendCard(MDCard):
    title = StringProperty("")
    subtitle = StringProperty("")
    image_icon = StringProperty("album")


class HomeScreen(MDScreen):
    def open_player(self, title, artist, duration):
        player = self.manager.get_screen("player")
        player.load_song(title, artist, duration)
        self.manager.current = "player"

    def go_home(self):
        self.manager.current = "home"

    def go_search(self):
        self.manager.current = "search"

    def go_favorite(self):
        favorite_screen = self.manager.get_screen("favorite")
        favorite_screen.refresh_favorites()
        self.manager.current = "favorite"

    def go_profile(self):
        profile_screen = self.manager.get_screen("profile")
        profile_screen.refresh_profile()
        self.manager.current = "profile"