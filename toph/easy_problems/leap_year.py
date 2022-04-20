""" find leap year"""
Y = int(input())


def is_leap(n):
    # Leap Year Check
    if Y % 4 == 0 and Y % 100 != 0:
        print("Yes")
    elif Y % 100 == 0:
        print("No")
    elif Y % 400 == 0:
        print("Yes")
    else:
        print("No")


is_leap(Y)
