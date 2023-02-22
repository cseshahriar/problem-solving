# factorial with math lib
import math
n = int(input())
result = math.factorial(n)
print(result)

# factorial with for loop
factorial = 1
if n >= 1:
    for i in range(1, n+1):
        factorial = factorial * i
print(factorial)
