n = int(input('Enter N '))

def fibonacci(n):
    if n < 0:
        print("incorrect")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(n)
print(f"The fibonacci series for {n} is {result}")

# Sub array
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray = []
for i in range(len(arr)):
    subarray.append(arr[0:i])

print(subarray)
    
