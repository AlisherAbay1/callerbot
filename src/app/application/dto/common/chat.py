from dataclasses import dataclass


@dataclass
class ChatDTO:
    tg_id: int
    is_registered: bool
    emoji: str
