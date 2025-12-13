import random

from game.author_randomiser import AuthorRandomiser
from game.challenge import Challenge
from game.challenges import CHALLENGES


class ChallengeRandomiser:

    def __init__(self):
        self.active_challenges: list[Challenge] = []
        self.remaining_challenges = list(CHALLENGES)
        self.author_randomiser = AuthorRandomiser(
            self._unique_authors(self.remaining_challenges)
        )

    def _unique_authors(self, challenges: list[Challenge]):
        return list(set(challenge.author for challenge in challenges))

    def reset(self):
        self.remaining_challenges.extend(self.active_challenges)
        self.active_challenges.clear()

    def add(self):
        author_choices = self._unique_authors(self.remaining_challenges)
        author = self.author_randomiser.choice(author_choices)
        challenge_choices = [
            challenge
            for challenge in self.remaining_challenges
            if challenge.author == author
        ]
        challenge = random.choice(challenge_choices)
        self.active_challenges.append(challenge)
        self.remaining_challenges.remove(challenge)

    def challenges(self):
        if not self.active_challenges:
            return "no active challenges"
        return "current challenges:\n" + "\n".join(
            f"- {challenge.author}: {challenge.description}"
            for challenge in self.active_challenges
        )
