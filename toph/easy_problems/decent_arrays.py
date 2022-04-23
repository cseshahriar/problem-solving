""" decent arrays """
n = int(input())
A = list(map(int, input().split()))
    
data2 = sorted(A)

if data2 == A:
    print('Yes')
else:
    print('No')