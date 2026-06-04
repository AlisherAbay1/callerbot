from callerbot.application.dto.common import ChatMemberDTO
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserWithChatsDTO:
    tg_id: int
    is_globally_registered: bool
    global_emoji: Optional[str]

    chats: list[ChatMemberDTO]
