""" is anagram """
A = input()
B = input()

def check(a, b):
	if(sorted(a) == sorted(b)):
		print('Yes')
	else:
		print('No')

check(A, B)