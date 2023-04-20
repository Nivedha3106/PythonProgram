# Write a program that prints a countdown for your birthday

import datetime

today = datetime.date.today()

user_birth_year = int(input("Enter year of birth i.e. 1989: "))
user_birth_month = int(input("Enter month of birth i.e. for June enter 6: "))
user_birth_day = int(input("Enter day of birth i.e. for 21st enter 21: "))

my_birthday = datetime.date(today.year, user_birth_month, user_birth_day)
if my_birthday == today:
    print("Happy Birthday!")
else:
    if my_birthday < today:
        my_birthday = my_birthday.replace(year=today.year + 1)
        days_until_birthday = my_birthday - today
        print(days_until_birthday)

    else:
        days_until_birthday = my_birthday - today
        print(days_until_birthday)