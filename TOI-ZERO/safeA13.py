char = input()
num = int(input())
if char == "H" and num == 4567:
    print("safe unlocked")
elif char == "H":
    print("safe locked - change digit")
elif num == 4567:
    print("safe locked - change char")
else:
    print("safe locked")