from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int

class UserInCreate(BaseModel):
    username: str
    password: str
    balance: int