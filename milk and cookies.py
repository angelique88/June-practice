import datetime

print("Is it time for milk and cookies?")

while True:
    year = input("Enter a year: ")
    try:
        int(year)
        break
    except:
        print("Input numerical values ")
        continue

while True:
    month = input("Enter a month: ")
    try:
        int(month)
        break
    except:
        print("Input numerical values ")
        continue

while True:
    day = input("Enter a day: ")
    try:
        int(day)
        break
    except:
        print("Input numerical values ")
        continue

date = (year, month, day)

if (date[1] == '12') and (date[2] == '24'):
    print("It is Christmas Eve! Time for milk and cookies!")
else:
    print("It is not Christmas Eve! No milk and cookies!")