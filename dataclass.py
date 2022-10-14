
from dataclasses import field, dataclass

@dataclass
class User:
  name: str
  age: int
  items: list[int] = field(default_factory=list)
  
user = User('sato', 20)
print(user.name)
print(user.age)
print(user.items)
