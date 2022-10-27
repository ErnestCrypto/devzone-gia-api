# creating our custom id generating function for
import secrets
import random


def custom_id():
    random_number = random.randint(
        10000000000, 99999999999999999999) + random.randint(10000000000, 99999999999999999999) + random.randint(10000000000, 99999999999999999999)
    unique_id = "GIA-" + str(random_number)
    return unique_id


def transaction_id():
    return secrets.token_hex(32)
