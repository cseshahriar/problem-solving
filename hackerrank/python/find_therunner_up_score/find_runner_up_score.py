if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    z = max(arr) 
    i = 0

    while(i<n):
        if z == max(arr):
            arr.remove(max(arr))
        i += 1
    print(max(arr))