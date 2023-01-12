T = int(input())


def trailing_zeros(data):
    data_str = str(data)
    return len(data_str) - len(data_str.rstrip('0'))


for i in range(T):
    n = int(input())
    factorial = 1
    for j in range(1, n+1):
        factorial *= j
    print(trailing_zeros(factorial))
