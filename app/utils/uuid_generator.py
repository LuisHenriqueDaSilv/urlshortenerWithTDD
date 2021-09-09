import string
import random

def uuid_generator(size=6) -> str:
    chars = string.ascii_lowercase + string.digits
    uuid = ''.join(random.choice(chars) for _ in range(size))
    return uuid
