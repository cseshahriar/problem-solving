"""subarray sum """
n, index_a, index_b = list(map(int, input().split()))
data = list(map(int, input().split()))

sub_array = data[index_a:index_b+1]
print(sum(sub_array))
