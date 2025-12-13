class Challenge:

    def __init__(self, author: str, description: str):
        self.author = author
        self.description = description

    @classmethod
    def from_file(cls, data: str):
        author, description = data.split(":")
        return Challenge(author.strip(), description.strip())
