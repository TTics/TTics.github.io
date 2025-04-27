a=int(input())
mi,ma=2e9,-2e9
for i in range(a):
    b=int(input())
    mi = min(mi, b)
    ma = max(ma, b)
print(mi)
print(ma)