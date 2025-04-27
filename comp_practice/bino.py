import math
n, r= [int(i) for i in input().split()]
print(n, r)
print(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))