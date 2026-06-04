from dataclasses import dataclass


@dataclass
class ChatMemberDTO:
    tg_id: int
    chat_title: str
    is_registered: bool
    emoji: str
