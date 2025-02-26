import re


def check_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    return True


password = input("Введите пароль: ")
if check_password(password):
    print("Пароль безопасен!")
else:
    print("Пароль небезопасен!")
