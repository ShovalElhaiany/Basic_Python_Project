from dataclasses import *


@dataclass
class Customer:
    id: int
    name: str
    city: str
    age: int
