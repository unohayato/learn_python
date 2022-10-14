
from dataclasses import field, dataclass
import dataclasses

@dataclass
class User:
  name: str
  age: int
  items: list[int] = field(default_factory=lambda: ['note', 'pen'])
  
user = User('sato', 20)
print(user.name)
print(user.age)
print(user.items)

class User2:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
user1 = User2('u', 20)
user2 = User2('u', 20)
print(user1 == user2)

@dataclass
class User3:
  name: str
  age: int
user3 = User3('u', 30)
user4 = User3('u', 30)

print(user3 == user4)

@dataclass
class User4:
  name: str
  age: int

user5 = User4('t', 40)
user5 = dataclasses.asdict(user5)
print(user5)
