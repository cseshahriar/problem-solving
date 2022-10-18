n = int(input('Enter the number of N '))

# first two terms
n_1 = 0
n_2 = 1
count = 0

# now, we will check if the number of terms is valid or not
if n <= 0:
    print('Please enter a positive integer, the given is number not valid.')
elif n == 1:
    print('The fibonacci sequence of the numbers of up to ', n)
    print(n_1)
else:
    print('the fibonacci sequence of the numbers is: ')
    while count < n:
        print(n_1)
        nth = n_1 + n_2
        # at last, we will update values
        n_1 = n_2
        n_2 = nth
        count += 1
