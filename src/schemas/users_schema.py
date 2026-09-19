from pydantic import BaseModel,Field

class User(BaseModel):

    name:str=Field(min_length=2)
    email:str
    password:str=Field(min_length=6)