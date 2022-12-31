# Bismillahhir Rahmanir Rahim
T = int(input())

def find_divisors(n):
    """ return all divisors for a n"""
    text = ""
    for i in range(1, n + 1):
        if n % i == 0:
            text += f"{i} "
    return  text

for i in range(1, T+1):
    number = int(input())
    print(f"Case {i}: ", end="")
    divisors = find_divisors(number)
    print(divisors)