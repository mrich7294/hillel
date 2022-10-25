import sys

year = int(input("Enter the number of years: "))
if (year > 1900) and (year < 1000000):
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    elif year % 4 == 0:
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
else:
    print("Enter the number of years is not correct!")
    sys.exit()
