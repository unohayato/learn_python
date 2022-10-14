
from dataclasses import field, dataclass

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

