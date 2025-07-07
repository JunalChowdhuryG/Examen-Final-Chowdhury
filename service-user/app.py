from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="User Service")

users: Dict[int, Dict] = {}

class User(BaseModel):
    id: int      
    name: str    
    email: str 

@app.post("/users/", response_model=User)
def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user.dict()
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user.dict()
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"detail": "User deleted"}

@app.get("/health")
def health():
    return {"status": "ok"}