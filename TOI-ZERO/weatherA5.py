month = int(input())
day=int(input())
if month%3 == 0 and day >= 21:
    month += 1

if month < 4:
    print("winter")
elif month < 7:
    print("spring")
elif month < 10:
    print("summer")
elif month <13:
    print("fall")