from kivy.uix.screenmanager import Screen


class PlayerScreen(Screen):
    def back_home(self):
        print("[Callback] back_home triggered")
        self.manager.current = "home"

    def on_play(self):
        print("[Callback] on_play triggered -> Playing music...")

    def on_pause(self):
        print("[Callback] on_pause triggered -> Music paused.")

    def on_next(self):
        print("[Callback] on_next triggered -> Skipping to next song.")

    def on_prev(self):
        print("[Callback] on_prev triggered -> Going to previous song.")