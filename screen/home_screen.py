from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def open_player(self, song_id):
        print(f"[Callback] open_player triggered with Song ID: {song_id}")
        self.manager.current = "player"