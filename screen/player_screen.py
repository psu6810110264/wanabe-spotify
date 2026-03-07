from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class PlayerScreen(Screen):
    song_title = StringProperty("Midnight Dreams")
    artist_name = StringProperty("The Dreamers")
    current_song_id = StringProperty("song_1")

    songs = {
        "song_1": {
            "title": "Midnight Dreams",
            "artist": "The Dreamers",
        },
        "song_2": {
            "title": "Summer Vibes",
            "artist": "Beach Boys Revival",
        },
        "song_3": {
            "title": "Electric Soul",
            "artist": "Neon Lights",
        },
    }

    song_order = ["song_1", "song_2", "song_3"]

    def set_song(self, song_id):
        """ตั้งค่าเพลงปัจจุบันจาก song_id"""
        if song_id in self.songs:
            self.current_song_id = song_id
            self.song_title = self.songs[song_id]["title"]
            self.artist_name = self.songs[song_id]["artist"]
            print(f"[Callback] open_player triggered with Song ID: {song_id}")
        else:
            print(f"[Error] song_id not found: {song_id}")

    def on_play(self):
        print(f"[Callback] play triggered: {self.song_title}")

    def on_pause(self):
        print(f"[Callback] pause triggered: {self.song_title}")

    def on_prev(self):
        """เลื่อนไปเพลงก่อนหน้า"""
        current_index = self.song_order.index(self.current_song_id)
        prev_index = (current_index - 1) % len(self.song_order)
        prev_song_id = self.song_order[prev_index]
        self.set_song(prev_song_id)
        print(f"[Callback] prev triggered: {self.song_title}")

    def on_next(self):
        """เลื่อนไปเพลงถัดไป"""
        current_index = self.song_order.index(self.current_song_id)
        next_index = (current_index + 1) % len(self.song_order)
        next_song_id = self.song_order[next_index]
        self.set_song(next_song_id)
        print(f"[Callback] next triggered: {self.song_title}")

    def back_home(self):
        print("[Callback] back_home triggered")
        self.manager.current = "home"

    def add_favorite(self):
        """ตอนนี้เป็นเวอร์ชันทดสอบก่อน"""
        print(f"[Callback] add_favorite triggered: {self.song_title}")