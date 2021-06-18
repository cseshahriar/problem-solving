import itertools

s,n = list(map(str,input().split(' '))) # 
s = sorted(s)
# s	"HACK"
# n	"2"


for p in list(itertools.permutations(s,int(n))):
    print(''.join(p))