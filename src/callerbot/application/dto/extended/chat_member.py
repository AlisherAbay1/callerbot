from dataclasses import dataclass


@dataclass
class TagChatMembersDTO:
    user_tg_id: int
    user_emoji: str
