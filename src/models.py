USERS = []
next_id = 0

def create_user(data):
    global next_id
    user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"],
        "cargo": data["cargo"]
    }
    USERS.append(user)
    next_id += 1
    return user


def get_all_users():
    return USERS


def get_user_by_id(user_id):
    for user in USERS:
        if user["id"] == user_id:
            return user
    return None


def update_user(user_id, data):
    for user in USERS:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["cargo"] = data.get("cargo", user["cargo"])
            return user
    return None


def delete_user(user_id):
    global USERS
    for user in USERS:
        if user["id"] == user_id:
            USERS = [u for u in USERS if u["id"] != user_id]
            return user
    return None
