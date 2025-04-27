c = input()
lo, up = 0, 0
for i in c:
    if ord("a") <= ord(i) <= ord("z"):
        lo = 1
    elif ord("A") <= ord(i) <= ord("Z"):
        up = 1
if lo == 1 and up == 1:
    print("Mix")
elif lo == 1:
    print("All Small Letter")
elif up == 1:
    print("All Capital Letter")