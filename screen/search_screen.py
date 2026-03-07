from kivy.uix.screenmanager import Screen


class SearchScreen(Screen):
    def go_home(self):
        print("[Callback] search go_home triggered")
        self.manager.current = "home"

    def go_search(self):
        print("[Callback] search go_search triggered")
        self.manager.current = "search"

    def go_favorite(self):
        print("[Callback] search go_favorite triggered")
        self.manager.current = "favorite"