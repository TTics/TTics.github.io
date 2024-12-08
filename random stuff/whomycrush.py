import time
lol = input("Who do you think is my crush? (all lowercase) ")
bruh = 0
while bruh != 1:
     if lol == "uno" or lol == "me" or lol == "you":
        lol = input("WTF. Im not gay. Try again. ")
     elif len(lol) > 6:
        lol = input("You're just typing random stuff. Try again. ")
     elif lol == "you have no crush" or lol == "no crush" or lol == "none":
         print("Then why are you still here? get outta here.")
         print("The program will automatically close in 5 seconds.")
         time.sleep(5)
         break
         
         
     else:
        lol = input("No, not even close. Try again. ")
     