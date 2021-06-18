import itertools

ar1 = list(map(int,input().split())) # 1 2
ar2 = list(map(int,input().split())) # 3 4
cross = list(itertools.product(ar1,ar2)) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(cross)

for i in cross:
    print(i,end=' ')