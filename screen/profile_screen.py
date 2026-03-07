from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen

from data_store import get_current_user, get_favorites


class ProfileScreen(MDScreen):
    profile_username = StringProperty("Guest")
    profile_stats = StringProperty("0 favorite songs")

    def on_pre_enter(self, *args):
        self.refresh_profile()
        return super().on_pre_enter(*args)

    def refresh_profile(self):
        username = get_current_user() or "Guest"
        favorite_count = len(get_favorites())
        label = "song" if favorite_count == 1 else "songs"

        self.profile_username = username
        self.profile_stats = f"{favorite_count} favorite {label}"

    def go_home(self):
        self.manager.current = "home"
