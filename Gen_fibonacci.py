def gen_fib_seq(n):
    a = 0
    b = 1
    
    fib_seq = []
    
    if n <= 0:
        return "Number of terms must be a positive integer."
    
    for _ in range(n):
        fib_seq.append(a)
        c = a + b
        a = b
        b = c
    
    return fib_seq
  
num_terms = 10
print(gen_fib_seq(num_terms))
