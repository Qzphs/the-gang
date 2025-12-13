from game.challenge import Challenge


with open("challenges.txt") as file:
    CHALLENGES = [Challenge.from_file(line) for line in file.read().splitlines()]
