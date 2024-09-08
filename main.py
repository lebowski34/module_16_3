from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, example="UrbanUser")],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, example=24)]
):
    new_user_id = str(max(map(int, users.keys())) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {new_user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, example=1)],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, example="UrbanProfi")],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, example=28)]
):
    user_id = str(user_id)
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return {"message": f"User {user_id} has been updated"}
    return {"error": f"User {user_id} not found"}

@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, example=2)]):
    user_id = str(user_id)
    if user_id in users:
        del users[user_id]
        return {"message": f"User {user_id} has been deleted"}
    return {"error": f"User {user_id} not found"}
