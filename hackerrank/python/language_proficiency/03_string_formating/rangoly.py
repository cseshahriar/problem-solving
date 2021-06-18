def print_rangoli(n):
    n = int(n)
    w = (n-1) * 2 + ((n * 2) - 1) # formula: how much char will print
    #upper half
    for i in range(1, n, 1):
        number_of_letter = (i*2) - 1 # increment +=3 like 1, 3, 4, 5, 7
        s = ''
        letter_value = 97 + n - 1 # letter decimal values

        for i in range(0, number_of_letter):
            if(i != 0):
                s += '-' 
            s += chr(letter_value)
            if(i < (number_of_letter-1) / 2):
                letter_value = letter_value - 1 # decrement
            else:
                letter_value = letter_value + 1 # increment
               
        print(s.center(w,'-'))
        
        
    #bottom half
    for i in range(n,0,-1):
        number_of_letter = (i*2) - 1
        s = ''
        letter_value = 97 + n - 1
        for i in range(0,number_of_letter):
            if(i != 0):
                s += '-' 
            s += chr(letter_value) 
            if(i<(number_of_letter-1) / 2):
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1            
        print(s.center(w,'-'))

        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)