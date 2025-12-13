import random


class AuthorRandomiser:
    """Bag randomiser for challenge authors."""

    def __init__(self, authors: list[str]):
        self.options = authors
        self.remaining = authors.copy()

    def choice(self, authors: list[str]):
        choices = [author for author in authors if author in self.remaining]
        if not choices:
            self.remaining.clear()
            self.remaining.extend(self.options)
            choices = [author for author in authors if author in self.remaining]
        choice = random.choice(choices)
        self.remaining.remove(choice)
        return choice
