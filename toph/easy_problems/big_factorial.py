""" big factorials """
N = int(input())
fact = 1
j = -4

for i in range(1, N+1):
    fact = fact * i

num = fact

result = list(map(int, str(num)))  # int object is not iterable
if len(result) < 4:
    print(num)
else:
    while  True:
        print(result[j], end="")
        j = j + 1
        if j == 0:
            break

