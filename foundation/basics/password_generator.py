import random
import string


def password_gen():
    length = int(input("Enter length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Password:", password)


password_gen()
