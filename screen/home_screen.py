from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen

from data_store import get_current_user_role


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
    can_add_song = BooleanProperty(False)

    def on_pre_enter(self, *args):
        self.can_add_song = get_current_user_role() == "artist"
        return super().on_pre_enter(*args)

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

    def go_add_song(self):
        if get_current_user_role() != "artist":
            profile_screen = self.manager.get_screen("profile")
            profile_screen.notice_message = "Only Artist accounts can create songs."
            profile_screen.refresh_profile()
            self.manager.current = "profile"
            return

        add_song_screen = self.manager.get_screen("add_song")
        add_song_screen.refresh_song_list()
        self.manager.current = "add_song"