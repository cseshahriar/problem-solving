""" is prime number """
num = int(input())
if num > 1 and num < 1000:
    for i in range(2, num//2):
	    if(num % i) == 0:
		    print('No')
		    break
    else:
        print('yes')