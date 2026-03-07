from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from data_store import get_favorites


class FavoriteScreen(Screen):

    def on_pre_enter(self):
        self.load_favorites()

    def load_favorites(self):

        layout = self.ids.favorite_list
        layout.clear_widgets()

        favorites = get_favorites()

        if not favorites:
            layout.add_widget(Button(
                text="No favorite songs yet",
                size_hint_y=None,
                height=80
            ))
            return

        for song in favorites:

            btn = Button(
                text=song,
                size_hint_y=None,
                height=80,
                background_normal="",
                background_color=(0.12,0.12,0.14,1)
            )

            layout.add_widget(btn)

    def go_home(self):
        self.manager.current = "home"

    def go_search(self):
        self.manager.current = "search"

    def go_favorite(self):
        pass