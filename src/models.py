USERS = []
next_id = 0

def create_user(data):
    global next_id
    user = {
        "id" : next_id,
        "name" : data["name"],
        "email" : data["email"]
    }
    USERS.append(user)
    next_id +=1
    return user
def get_all_users():
    return USERS

def get_user_by_id(user_id):
    for user in USERS:
        if user["id"] == user_id:
            return user
    return None