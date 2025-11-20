1️ Age Calculator
from datetime import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

# Разница в годах, месяцах и днях
years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (birthdate.replace(year=today.year, month=today.month) - 
             birthdate.replace(year=today.year, month=today.month-1)).days

if months < 0:
    years -= 1
    months += 12

print(f"Your age: {years} years, {months} months, {days} days")

2️ Days Until Next Birthday
from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_remaining = (next_birthday - today).days
print(f"Days until next birthday: {days_remaining}")

3️ Meeting Scheduler
from datetime import datetime, timedelta

current_dt_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
current_dt = datetime.strptime(current_dt_str, "%Y-%m-%d %H:%M")

hours = int(input("Enter meeting duration hours: "))
minutes = int(input("Enter meeting duration minutes: "))

end_time = current_dt + timedelta(hours=hours, minutes=minutes)
print("Meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

4️ Timezone Converter
from datetime import datetime
import pytz

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

current_tz_str = input("Enter your current timezone (e.g., Europe/London): ")
target_tz_str = input("Enter target timezone (e.g., Asia/Tashkent): ")

current_tz = pytz.timezone(current_tz_str)
target_tz = pytz.timezone(target_tz_str)

dt = current_tz.localize(dt)
converted_dt = dt.astimezone(target_tz)

print("Converted date and time:", converted_dt.strftime("%Y-%m-%d %H:%M"))

5 Countdown Timer
from datetime import datetime
import time

future_dt_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_dt = datetime.strptime(future_dt_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future_dt - now
    if remaining.total_seconds() <= 0:
        print("Time's up!")
        break
    print(f"Time remaining: {remaining}", end="\r")
    time.sleep(1)

6️ Email Validator
import re

email = input("Enter your email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

7️ Phone Number Formatter
phone = input("Enter phone number (10 digits): ")
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print("Formatted phone number:", formatted)

8️ Password Strength Checker
import re

password = input("Enter your password: ")

length = len(password) >= 8
upper = bool(re.search(r'[A-Z]', password))
lower = bool(re.search(r'[a-z]', password))
digit = bool(re.search(r'\d', password))

if all([length, upper, lower, digit]):
    print("Strong password")
else:
    print("Weak password")

9️ Word Finder
text = """This is a sample text. You can search any word in this text."""
word = input("Enter the word to find: ")

positions = [i for i in range(len(text)) if text.startswith(word, i)]
print(f"Occurrences of '{word}':", positions)

10 Date Extractor
import re

text = input("Enter text with dates: ")
# Пример формата: YYYY-MM-DD или DD/MM/YYYY
pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b'
dates = re.findall(pattern, text)

print("Dates found:", dates)
