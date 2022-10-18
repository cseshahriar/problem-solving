# function for nth fibonacci numbers
n = int(input('Enter a number for N: '))


def fibonacci(n):
    if(n <= 0):
        print("incorrect input")
    # first fibonacci number is 0
    elif n == 1:
        return 0
    # second fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# diver program


print(fibonacci(n))
