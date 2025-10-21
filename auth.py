import json

def authenticate_user(username, password):
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False
