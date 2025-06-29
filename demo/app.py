from datetime import datetime

now = datetime.now()
today = now.strftime("20%y-%m-%d %H:%M:%S")

print(today)
print(type(today))
