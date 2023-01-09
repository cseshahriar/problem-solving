import math

def is_full_square(n):
    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)

def main():
    T = int(input())  # Read the number of test cases
    for i in range(T):
        n = int(input())  # Read the next test case
        if is_full_square(n):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
