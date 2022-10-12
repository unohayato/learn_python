
from dataclasses import dataclass

@dataclass
class User:
  name: str
  age: int
  
user = User('sato', 20)
print(user.name)
print(user.age)
