count = int(input())
name = []
weight = []
overweight = 0
for i in range(count):
    temp = input().split()
    temp_weight = int(temp[1])
    name.append(temp[0])
    weight.append(temp_weight)
    if weight[i] > 15:
        overweight +=1
print(overweight)
for i in range(count):
    if weight[i] == max(weight):
        print(f"{name[i]} {weight[i]}")