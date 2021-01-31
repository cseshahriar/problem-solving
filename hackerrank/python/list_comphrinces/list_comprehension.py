if __name__ == '__main__':
    x = input(input())
    y = input(input())
    z = input(input())
    n = input(input())

print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])