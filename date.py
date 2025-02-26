

def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
    today = datetime.today()
    age_in_days = (today - birth_date).days
    age_in_years = age_in_days // 365
    return age_in_years

def main():
    birth_date_str = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")
    age = calculate_age(birth_date_str)
    print(f"Вам {age} лет.")

if __name__ == "__main__":
    main()
