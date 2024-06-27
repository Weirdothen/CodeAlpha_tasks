def generate_fibonacci_sequence(n_terms):
    # Initialize the first two terms of the Fibonacci series
    fib_term1 = 0
    fib_term2 = 1
    
    # Create a list to store the Fibonacci sequence
    fibonacci_sequence = []
    
    # Check if the number of terms is less than or equal to 0
    if n_terms <= 0:
        return "Number of terms must be a positive integer."
    
    # Generate Fibonacci sequence for the given number of terms
    for _ in range(n_terms):
        fibonacci_sequence.append(fib_term1)
        next_term = fib_term1 + fib_term2
        fib_term1 = fib_term2
        fib_term2 = next_term
    
    return fibonacci_sequence

# Example usage: Generate the first 10 terms of the Fibonacci sequence
number_of_terms = 10
print(generate_fibonacci_sequence(number_of_terms))
