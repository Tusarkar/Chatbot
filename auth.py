from users import VALID_USERS, hash_password

def authenticate(email, password):
    hashed_password = VALID_USERS.get(email)
    return hashed_password == hash_password(password)
