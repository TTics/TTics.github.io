m, n = (int(i) for i in input().split())
# print(m, n)
a = []
r = []
for i in range(m):
    b=[int(i) for i in input().split()]
    a.append(b)
for i in range(m):
    b=[int(i) for i in input().split()]
    r.append(b)
for i in range(m):
    for j in range(n):
        print(a[i][j]+r[i][j], end=" ")
    print()

'''
3 3
1 2 3
3 2 1
1 3 2
1 1 1
1 1 1
1 1 1

a[i][j] += b[i][j]
'''