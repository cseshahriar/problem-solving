n = int(input())


# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    # Initialize first two terms
    a, b = 0, 1
    # List to store the sequence
    fib_sequence = []
    # Loop through n terms
    for i in range(n):
        # Append the current term to the sequence
        fib_sequence.append(a)
        # Update the first two terms to generate the next term
        a, b = b, a + b
    # Return the generated sequence
    return fib_sequence


# Example usage
print(fibonacci(n)) # Generate first 10 terms of the Fibonacci sequence
