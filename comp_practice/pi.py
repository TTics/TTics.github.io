pi = 0
count = 0
gay = 1
for i in range(10000000000):
    if count%2 == 0:
        pi += 4/gay
    if count%2 == 1:
        pi -= 4/gay
    gay+=2
    count+=1
print(pi)