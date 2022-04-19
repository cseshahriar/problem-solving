"""
fibonacci numbers
Fn = Fn-1 + Fn-2
F0 = 0 and F1 = 1
"""
n = int(input())

def fibonacci(n):
    if n >= 0 and n < 50:
        fib_arr = [0, 1]
        # fib_arr.extend(fib_arr[i-1] + fib_arr[i-2] for i in range(2, n + 1))
        for i in range(2, n + 1):
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])
        return fib_arr[n]


result = fibonacci(n)
print(result)
