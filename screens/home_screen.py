from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def go_home(self):
        print("Home")

    def go_search(self):
        print("Search (todo)")

    def go_favorite(self):
        print("Favorite (todo)")

    def on_search(self, text):
        print("Search:", text)

    def open_player(self, song_name):
        print("Open player:", song_name)