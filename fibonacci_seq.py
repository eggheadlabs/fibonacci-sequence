# Generate N Fibonacci numbers in recursion
# Example: first 10 Fibbonacci numbers: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

from functools import lru_cache

@lru_cache(maxsize=1000)        # use Python built-in least-recently-used cache module
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-2) + fibonacci(n-1)

s = input('How many Fibonacci numbers to be generated: ')
N = int(s)
if N < 1: raise ValueError('N must be a positive integer')

for n in range (1, N+1):
    print(str(n) + '\t:', fibonacci(n))