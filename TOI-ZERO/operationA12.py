number = input()
operation = input()
reverse = number[1] + number[0]
intreverse = int(reverse)
intnumber = int(number)

if operation == "+":
    result = intnumber + intreverse
    print(f"{intnumber} + {intreverse} = {result}")
elif operation == "*":
    result = intnumber * intreverse
    print(f"{intnumber} * {intreverse} = {result}")