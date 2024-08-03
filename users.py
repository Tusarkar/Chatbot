import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Define hashed passwords
VALID_USERS = {
    "user1@example.com": hash_password("password1"),
    "user2@example.com": hash_password("password2"),
    "user3@example.com": hash_password("password3"),
}
