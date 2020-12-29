from admin import Admin


def authenticate(username, password):
    user = Admin.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    user_id=payload['identity']
    return Admin.find_by_id(user_id)