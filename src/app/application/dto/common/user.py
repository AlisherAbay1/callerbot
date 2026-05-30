from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    tg_id: int
    is_globally_registered: bool
    global_emoji: Optional[str]
