'''
August Doe
10/22/24
Unit 2 and 3 project
'''

month = input("Enter the name of the month: ")
month = month.title()
day = int(input("Enter the day (1-31): "))
if month == "January" or month == "February" or month == "March" and 1 <= day < 20 or month == "December" and 21 <= day <= 31:
    print(f"{month} {day} is in Winter")
if month == "March" and 20 <= day <= 31 or month == "April" or month == "May" or month == "June" and 1 <= day < 21:
    print(f"{month} {day} is in Spring")
if month == "June" and 21 <= day <= 31 or month == "July" or month == "August" or month == "September" and 1 <= day < 22:
    print(f"{month} {day} is in Summer")
if month == "September" and 22 <= day <= 31 or month == "October" or month == "November" or month == "December" and 1 <= day < 21:
    print(f"{month} {day} is in Fall")