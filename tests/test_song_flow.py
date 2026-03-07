from kivy.app import App
from kivymd.app import MDApp

from data_store import add_custom_song, custom_songs, get_song_file, get_song_lyrics
from screen.player_screen import PlayerScreen


class DummySound:
    def __init__(self):
        self.length = 120
        self.play_calls = 0
        self.stop_calls = 0
        self.position = 0

    def play(self):
        self.play_calls += 1

    def stop(self):
        self.stop_calls += 1
        self.position = 0

    def seek(self, seconds):
        self.position = seconds

    def get_pos(self):
        return self.position


class DummyMDApp(MDApp):
    def build(self):
        return None


def setup_function():
    custom_songs.clear()
    App._running_app = DummyMDApp()


def teardown_function():
    custom_songs.clear()
    App._running_app = None


def test_create_song_and_resolve_audio_file(tmp_path):
    audio_file = tmp_path / "demo_track.mp4"
    audio_file.write_bytes(b"fake mp4")

    success, _ = add_custom_song(
        title="Demo Track",
        artist="Demo Artist",
        duration="3:20",
        category="Pop",
        album="Singles",
        cover_image_path="cover.png",
        audio_file_path=str(audio_file),
    )

    assert success is True
    assert len(custom_songs) == 1
    assert custom_songs[0]["title"] == "Demo Track"
    assert get_song_file("Demo Track", "Demo Artist") == str(audio_file)


def test_create_song_stores_lyrics(tmp_path):
    audio_file = tmp_path / "demo_track.mp4"
    audio_file.write_bytes(b"fake mp4")

    success, _ = add_custom_song(
        title="Lyric Track",
        artist="Demo Artist",
        duration="3:00",
        category="Pop",
        album="Singles",
        cover_image_path="cover.png",
        audio_file_path=str(audio_file),
        lyrics="first line\\nsecond line",
    )

    assert success is True
    assert custom_songs[0]["lyrics"] == "first line\\nsecond line"
    assert get_song_lyrics("Lyric Track", "Demo Artist") == "first line\\nsecond line"


def test_player_can_load_and_toggle_play_for_custom_song(tmp_path, monkeypatch):
    audio_file = tmp_path / "demo_track.mp4"
    audio_file.write_bytes(b"fake mp4")

    add_custom_song(
        title="Demo Track",
        artist="Demo Artist",
        duration="3:20",
        category="Pop",
        album="Singles",
        cover_image_path="cover.png",
        audio_file_path=str(audio_file),
    )

    dummy_sound = DummySound()

    monkeypatch.setattr("screen.player_screen.SoundLoader.load", lambda path: dummy_sound)

    player = PlayerScreen()
    player.load_song("Demo Track", "Demo Artist", "3:20")

    assert player.current_sound is dummy_sound
    assert player.song_title == "Demo Track"
    assert player.playback_status == ""

    player.toggle_play_pause()
    assert player.is_playing is True
    assert dummy_sound.play_calls == 1

    player.toggle_play_pause()
    assert player.is_playing is False
    assert dummy_sound.stop_calls == 1


def test_player_sets_message_when_audio_backend_cannot_load(tmp_path, monkeypatch):
    audio_file = tmp_path / "demo_track.mp4"
    audio_file.write_bytes(b"fake mp4")

    add_custom_song(
        title="Broken Track",
        artist="Demo Artist",
        duration="3:20",
        category="Pop",
        album="Singles",
        cover_image_path="cover.png",
        audio_file_path=str(audio_file),
    )

    monkeypatch.setattr("screen.player_screen.SoundLoader.load", lambda path: None)
    monkeypatch.setattr("screen.player_screen.PlayerScreen._load_mp4_with_ffpyplayer", lambda self, path: None)

    player = PlayerScreen()
    player.load_song("Broken Track", "Demo Artist", "3:20")

    assert player.current_sound is None
    assert player.playback_status == "Cannot play .mp4 on this device. Install ffpyplayer and restart app."

    player.toggle_play_pause()
    assert player.is_playing is False
    assert player.playback_status == "No audio loaded"
