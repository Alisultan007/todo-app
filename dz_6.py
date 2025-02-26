import time

seconds = int(input("Введите количество секунд: "))

while seconds > 0:
    print(f"Осталось: {seconds} секунд...")
    time.sleep(1)
    seconds -= 1

print("Время вышло!")
