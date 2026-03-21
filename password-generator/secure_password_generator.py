import string
import secrets

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

print("=== Secure Password Generator ===")

user_length = int(input("Enter desired password length: "))
new_password = generate_password(user_length)

print("Your secure password is:")
print(new_password)
