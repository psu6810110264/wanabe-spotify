from kivy.app import App
from kivy.uix.label import Label

class WanabeSpotifyApp(App):
    def build(self):
        return Label(text="Wanabe Spotify - Initial Setup")

if __name__ == "__main__":
    WanabeSpotifyApp().run()