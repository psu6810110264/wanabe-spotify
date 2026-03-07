from kivy.uix.screenmanager import Screen


class FavoriteScreen(Screen):
    def go_home(self):
        print("[Callback] favorite go_home triggered")
        self.manager.current = "home"

    def go_search(self):
        print("[Callback] favorite go_search triggered")
        self.manager.current = "search"

    def go_favorite(self):
        print("[Callback] favorite go_favorite triggered")
        self.manager.current = "favorite"

    def open_player(self, song_id):
        print(f"[Callback] favorite open_player triggered with Song ID: {song_id}")

        player_screen = self.manager.get_screen("player")

        if song_id == "song_1":
            player_screen.song_title = "Midnight Dreams"
            player_screen.artist_name = "The Dreamers"
        elif song_id == "song_2":
            player_screen.song_title = "Summer Vibes"
            player_screen.artist_name = "Beach Boys Revival"
        elif song_id == "song_3":
            player_screen.song_title = "Electric Soul"
            player_screen.artist_name = "Neon Lights"
        else:
            player_screen.song_title = "Unknown Song"
            player_screen.artist_name = "Unknown Artist"

        self.manager.current = "player"