# Bismillahhir Rahmanir Rahim
T = int(input())
for i in range(1, T+1, 1):
    n = int(input())
    for _ in range(1, n + 1):
        print(n * "*")
    if i < T:
        print()