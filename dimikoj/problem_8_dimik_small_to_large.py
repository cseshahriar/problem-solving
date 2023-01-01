# Bismillahhir Rahmanir Rahim
T = int(input())
for i in range(1, T+1, 1):
    data = list(map(int, input().split()))
    data.sort()
    text = f"Case {i}: "
    text += " ".join(str(el) for el in data)
    print(text)