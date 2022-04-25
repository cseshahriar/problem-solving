"""subarray sum """
n = int(input())
index_a = int(input())
index_b = int(input())

data = []
for i in range(n):
    numbr = int(input())
    data.append(numbr)

result = sum(data[index_a:index_b+1])
print(result)
