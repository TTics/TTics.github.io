count = int(input())
id1 = input()
id2 = input()
intid1 = []
intid2 = []
matchcount = 0
for i in range(count):
    intid1.append(id1[i])
    intid2.append(id2[i])
for i in range(count):
    if int(intid1[i]) + int(intid2[i]) == 9:
        matchcount+=1
        
if matchcount == count:
    print("YES")
else:
    print(f"NO {count-matchcount}")