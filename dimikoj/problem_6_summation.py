# Bismillahhir Rahmanir Rahim
T = int(input())
for i in range(1, T+1, 1):
    data = list(map(int, input()))
    print("Sum =", data[0] + data[-1])