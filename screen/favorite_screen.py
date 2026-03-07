from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

from data_store import get_favorites
from screen.home_screen import SongCard


class FavoriteScreen(MDScreen):
    def on_pre_enter(self, *args):
        self.refresh_favorites()

    def refresh_favorites(self):
        container = self.ids.favorite_list
        container.clear_widgets()

        favorite_items = get_favorites()

        if not favorite_items:
            empty_label = MDLabel(
                text="No favorite songs yet",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                height=50,
            )
            container.add_widget(empty_label)
            return

        for index, item in enumerate(favorite_items, start=1):
            card = SongCard(
                title=item["title"],
                artist=item["artist"],
                rank=f"{index:02d}",
                duration=item["duration"],
                image_icon="heart"
            )
            card.bind(
                on_release=lambda instance, t=item["title"], a=item["artist"], d=item["duration"]: self.open_player(t, a, d)
            )
            container.add_widget(card)

    def open_player(self, title, artist, duration):
        player = self.manager.get_screen("player")
        player.load_song(title, artist, duration)
        self.manager.current = "player"

    def go_home(self):
        self.manager.current = "home"

    def go_search(self):
        self.manager.current = "search"

    def go_favorite(self):
        self.refresh_favorites()
        self.manager.current = "favorite"