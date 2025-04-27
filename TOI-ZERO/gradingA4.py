small = int(input())
medium = int(input())
big = int(input())
sscore = small/10
mscore = medium/40
bscore = big/50
if sscore < 0.5 or mscore < 0.5 or bscore < 0.5:
    print("fail")
else:
    print("pass")