n, m = [int(i) for i in input().split()]
a = []
path = []
mk = [[0 for i in range(m)] for j in range(n)]
# print(mk)
ansp = []
ch = 0
def play(i, j):
    # print(i, j, mk[i][j])
    if i < 0 or j < 0 or i >= n or j >=m:
        return 

    if a[i][j] == '#' or mk[i][j] == 1:
        # print(i, j, mk[i][j])
        return 

    if a[i][j] == 'E':
        print(path)
        ch = 1
        exit(0)
        # if ch == 0:
        #     ansp = path



    mk[i][j] = 1
    # print(i, j)
    path.append((i+1, j))
    play(i+1,j)
    path.pop()
    path.append((i, j+1))
    play(i,j+1)
    path.pop()
    path.append((i-1, j))
    play(i-1,j)
    path.pop()
    path.append((i, j+-11))
    play(i,j-1)
    path.pop()
    mk[i][j] = 0
    return 

for i in range(n):
    a.append(input())
# print("\n".join(a))
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            si, sj = i, j
            path.append((i, j))
# print(si, sj)

ans = play(si, sj)
print("true" if ch == 1 else "False")



'''
5 10
##########
..S#......
...#....E.
...#......
..........

'''