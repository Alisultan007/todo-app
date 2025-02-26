from datetime import datetime

birth_date = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
birth_date = datetime.strptime(birth_date, "%d.%m.%Y")


today = datetime.today()

т
age = today.year - birth_date.year


if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Вам {age} лет.")