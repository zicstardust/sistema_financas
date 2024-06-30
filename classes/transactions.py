from dataclasses import dataclass
from .tag import Tag

@dataclass
class Transaction:
    description: str
    value: float
    tag: Tag

    def show(self):
        print(
            f"Description: {self.description}\nValue: {self.value}\nTag: {self.tag.name}"
        )