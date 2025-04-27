a=int(input())
b=int(input())
c=int(input())
d=a+b+c
if d > 79:
    print("A")
elif d > 74:
    print("B+")
elif d > 69:
    print("B")
elif d > 64:
    print("C+")
elif d > 59:
    print("C")
elif d > 54:
    print("D+")
elif d > 49:
    print("D")
else:
    print("F")