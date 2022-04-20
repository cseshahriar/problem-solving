""" devisors """
A = int(input())
for x in range(1, A+1):
	if A % x == 0:
		print(x)