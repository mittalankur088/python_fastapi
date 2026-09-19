from fastapi import HTTPException
from src.schemas.users_schema import User

fake_db = []  # placeholder until you connect a real database


async def register_user(db,data:User):
    if any(u["email"] == data.email for u in fake_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = {"id": len(fake_db) + 1, "name": data.name, "email": data.email}
    fake_db.append(user)
    return user