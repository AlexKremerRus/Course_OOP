from typing import Any
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    flags: list
    comment: Any

class Test(User):
    pass