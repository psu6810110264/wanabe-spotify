from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from screen.home_screen import HomeScreen
from screen.player_screen import PlayerScreen

Window.size = (360, 640)

class SongCard(MDCard):
    title = StringProperty("")
    artist = StringProperty("")
    rank = StringProperty("")
    duration = StringProperty("")
    image_icon = StringProperty("music-note")

class RecommendCard(MDCard):
    title = StringProperty("")
    subtitle = StringProperty("")
    image_icon = StringProperty("album")

class MiniSpotifyApp(MDApp):
    def build(self):
       
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple" 
        return Builder.load_file('mini_spotify.kv')

if __name__ == '__main__':
    MiniSpotifyApp().run()