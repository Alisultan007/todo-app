from datetime import datetime, timedelta

days = int(input("number of days: "))
today = datetime.today()
future_date = today + timedelta(days=days)
print(future_date)
