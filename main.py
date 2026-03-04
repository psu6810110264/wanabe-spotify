from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

# กำหนดขนาดหน้าจอจำลองมือถือ
Window.size = (360, 640)

# สร้าง Class สำหรับการ์ดเพลง (แถวยาว)
class SongCard(MDCard):
    title = StringProperty("")
    artist = StringProperty("")
    rank = StringProperty("")
    duration = StringProperty("")
    image_icon = StringProperty("music-note")

# สร้าง Class สำหรับการ์ดแนะนำ (สี่เหลี่ยมจัตุรัส)
class RecommendCard(MDCard):
    title = StringProperty("")
    subtitle = StringProperty("")
    image_icon = StringProperty("album")

class MiniSpotifyApp(MDApp):
    def build(self):
        # ตั้งค่าธีมหลัก
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple" # สีหลักม่วง
        return Builder.load_file('mini_spotify.kv')

if __name__ == '__main__':
    MiniSpotifyApp().run()