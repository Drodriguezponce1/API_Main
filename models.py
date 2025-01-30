from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    email: Optional[str] = None

    def toStr(self):
        return f'User {self.name} is {self.age} years old'
    
    def updateID(self,id):
        self.id = id
        return
    
    def getId(self):
        return self.id