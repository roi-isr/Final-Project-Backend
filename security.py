""" Security & authentication class, for adding a layer of security to the application, and authenticating admins """

from admin import Admin


# Routes from app.py JWT instance object - implement the authentication of admins (sending them auth token for
# current session)
def authenticate(username, password):
    user = Admin.find_by_username(username)
    if user and user.password == password:
        return user

# Routes from app.py JWT instance object - used to verify authenticated users.
def identity(payload):
    user_id=payload['identity']
    return Admin.find_by_id(user_id)