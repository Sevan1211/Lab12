import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power(tv):
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute(tv):
    tv.power()
    tv.volume_up()  # Increase volume once
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up(tv):
    tv.channel_up()  # Test when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()  # Increase channel when TV is on
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    # Increase channel past maximum value
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down(tv):
    tv.channel_down()  # Test when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_down()  # Decrease channel when TV is on
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    # Decrease channel past minimum value
    for _ in range(4):
        tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up(tv):
    tv.volume_up()  # Test when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()  # Increase volume when TV is on
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    tv.volume_up()  # Increase volume when TV is muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Increase volume past maximum value
    for _ in range(3):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down(tv):
    tv.volume_down()  # Test when TV is off
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()  
    tv.volume_down()  # Decrease volume when TV is on
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    tv.volume_down()  # Decrease volume when TV is muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Decrease volume to minimum
    for _ in range(3):
        tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_muted_volume_adjustment(tv):
    tv.power()
    tv.volume_up() 
    tv.mute()  # Mute TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    # Increase volume when TV is muted
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    # Decrease volume when TV is muted
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

