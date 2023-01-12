T = int(input())
for i in range(1, T+1):
    n = int(input())
    factorial = 1
    for j in range(1, n+1):
        factorial *= j
    print(factorial)

