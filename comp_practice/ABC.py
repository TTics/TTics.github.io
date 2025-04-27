a=[]
for i in (input().split()):
    a.append(int(i))
a.sort()
b=input().split()
for i in range(3):
    if i=="A":
        print(a[0], end=" ")
    if i=="B":
        print(a[1], end=" ")
    if i=="C":
        print(a[2], end=" ")