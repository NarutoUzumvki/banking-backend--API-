import random
import string 

characters = string.ascii_letters + string.digits

def generate_account_no(length=12):
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def generate_transaction_id(length=6):
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string