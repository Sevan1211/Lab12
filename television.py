class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    temp: int = 0

    def __init__(self) -> None:
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        self._status = not self._status
        if not self._status:
            self._muted = False  

    def mute(self) -> None:
        if self._status:
            if not self._muted:
                self.temp = self._volume  
                self._muted = True
                self._volume = self.MIN_VOLUME  
            else:
                self._muted = False  
                self._volume = self.temp  

    def channel_up(self) -> None:
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL  
            else:
                self._channel += 1
                if self._muted:
                    self._muted = False  

    def channel_down(self) -> None:
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL  
            else:
                self._channel -= 1
                if self._muted:
                    self._muted = False  

    def volume_up(self) -> None:
        if self._status:
            if not self._muted:
                if self._volume < self.MAX_VOLUME:
                    self._volume += 1
            else:
                self._muted = False  
                self._volume = self.temp + 1

    def volume_down(self) -> None:
        if self._status:
            if not self._muted:
                if self._volume > self.MIN_VOLUME:
                    self._volume -= 1
            else:
                self._muted = False 
                self._volume = self.temp - 1  

    def __str__(self) -> str:
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

