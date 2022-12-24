# Bismillahhir Rahmanir Rahim
T = int(input())

def find_divisors(n):
    """ return all divisors for a n"""
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return  divisors

for i in range(1, T+1):
    number = int(input())
    print(f"Case {i}: ", end="")
    for j in range(1, number+1):
        if number % j == 0:
            print(j, end=' ')

    print("\n")