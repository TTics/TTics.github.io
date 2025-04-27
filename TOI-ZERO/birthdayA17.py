year1 = int(input())
month1 = int(input())
day1 = int(input())
year2 = int(input())
month2 = int(input())
day2 = int(input())
if year1 == year2 and month1 == month2 and day1 == day2:
    print("0")
elif year1 > year2:
    print("2")
elif year2 > year1:
    print("1")
elif year1 == year2:
    if month1 > month2:
        print("2")
    elif month1 < month2:
        print("1")
    elif month1 == month2:
        if day1 > day2:
            print("2")
        elif day1 < day2:
            print("1")