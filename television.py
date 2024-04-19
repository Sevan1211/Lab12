class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    temp = 0

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        self._status = not self._status
        if not self._status:
            self._muted = False  # Reset mute status when TV is turned off

    def mute(self):
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self.temp = self._volume
                self._volume = self.MIN_VOLUME
            else:
                self._volume = self.temp

    def channel_up(self):
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL  # Wrap around to the minimum channel
            else:
                self._channel += 1
                if self._muted:
                    self._muted = False  # Unmute TV when channel changes

    def channel_down(self):
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL  # Wrap around to the maximum channel
            else:
                self._channel -= 1
                if self._muted:
                    self._muted = False  # Unmute TV when channel changes

    def volume_up(self):
        if self._status:
            if not self._muted:
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1
            else:
                self._muted = False  # Unmute TV when volume changes
                self._volume = self.temp + 1

    def volume_down(self):
        if self._status:
            if not self._muted:
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1
            else:
                self._muted = False  # Unmute TV when volume changes
                self._volume = self.temp - 1 # Set volume to minimum

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
