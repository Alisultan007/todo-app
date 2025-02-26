from datetime import datetime

birth_date = input("Введите дату рождения в формате : ")
birth_date = datetime.strptime(birth_date, "%d.%m.%Y")


today = datetime.today()


age = (today - birth_date).days
a = int(age / 365)


print(f"Вам {a} лет.")