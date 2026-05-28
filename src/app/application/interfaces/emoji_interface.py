from typing import Protocol

class EmojiProtocol(Protocol):
    def get_random_emoji(self) -> str: ...