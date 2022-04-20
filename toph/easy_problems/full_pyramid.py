""" full pyramid """
N = int(input())
k = 0

for i in range(1, N+1):
    # print((N-i) + 1) so (5-1)+1 = 5, (5-2)+1 = 4, (5-3) + 1 = 3 , 2 , 1
    for space in range(1, (N-i) + 1):
        print(end="  ")

    # print(2*i-1)
    while k != (2*i-1):
        print("* ", end="")  # for first loop * print after 5 space both side
        k += 1

    k = 0
    print()