import random
import string


def generate_email():
    random_letter = random.choice(string.ascii_lowercase)
    random_number = random.randint(100, 999)
    email = f"{random_letter}{random_number}@yandex.ru"
    return email


def generate_password():
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=3))
    random_number = random.randint(100, 999)
    password = f"{random_letters}{random_number}"
    return password


def generate_name():
    random_length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_lowercase, k=random_length)).capitalize()
    return name


email = generate_email()
password = generate_password()
name = generate_name()

print(f"Email: {email}")
print(f"Password: {password}")
print(f"Name: {name}")


class UserAuthData:

    my_email = 'avanesov_vadim_9_123@yandex.ru'
    my_password = 'qwerty'
    my_username = 'Vadim'
