theos = input()
good = 1

for i in range(5):
    if i == 4:
        print(good, end="")
        print(theos[i], end="")
    elif theos[i] == theos[i+1]:
        good+=1
    else:
        print(good, end="")
        print(theos[i], end="")
        good = 1