from random_unicode_emoji import random_emoji


class Emoji:
    def get_random_emoji(self) -> str:
        return random_emoji(count=1)[0]
