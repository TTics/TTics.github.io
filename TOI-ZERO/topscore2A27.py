count = int(input())
score = []
maxcount = 0
maxsave = 0
for i in range(count):
    score.append(int(input()))

for i in range(count):
    if score[i] == max(score):
        maxsave = score[i]
        maxcount +=1
print(maxsave)
print(maxcount)