class StubPlayer:

    def play(self):
        return "playing"

    def stop(self):
        return "stopped"


def test_play():
    player = StubPlayer()
    assert player.play() == "playing"


def test_stop():
    player = StubPlayer()
    assert player.stop() == "stopped"