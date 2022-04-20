""" full pyramid """
size = int(input())

for i in range(size):
    for j in range((size-i) - 1):
        print(end=" ")

    for k in range(i+1):
        print("*", end="")
        if k < i:
            print(' ', end='')
    print()
