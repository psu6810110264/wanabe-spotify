from kivymd.uix.screen import MDScreen


class SearchScreen(MDScreen):
    def go_home(self):
        self.manager.current = "home"

    def go_search(self):
        self.manager.current = "search"

    def go_favorite(self):
        favorite_screen = self.manager.get_screen("favorite")
        favorite_screen.refresh_favorites()
        self.manager.current = "favorite"

    def open_player(self, title, artist, duration):
        player = self.manager.get_screen("player")
        player.load_song(title, artist, duration)
        self.manager.current = "player"