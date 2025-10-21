"""
Problem 3: Project Euler

The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143?
"""

# Used Decorateor

import math

def large_prime(func):
    def warpper(num):
        factors = func(num)
        for factor in reversed(factors):
            if factor < 2:
                continue
            isprime = True
            for i in range(2, int(math.sqrt(factor)) + 1):
                if factor % i == 0:
                    isprime = False
                    break
            if isprime:
                return factor              
    return warpper

@large_prime
def find_factors(num):
    factors=[]
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            factors.append(i)
            if i != (num // i):
                factors.append(num // i)
    return sorted(factors)

num = 600851475143
print(find_factors(num))

