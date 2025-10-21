"""
Problem 5: Project Euler

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.
"""

# Approach 1: Brute-force search using return
num_list = list(range(1,21))
def evenly_divisible(num):
    while True:
        for i in num_list:
            if num % i != 0:
                break
        else:
            return num
        num +=1                        
print(evenly_divisible(2520))


# Approach 2: Brute-force search using a generator (yield)
num_list = list(range(1, 21))
def evenly_divisible(num):
    while True:
        for i in num_list:
            if num % i != 0:
                break
        else:
            yield num
        num += 1
gen = evenly_divisible(2520)
print(next(gen))

# Approach 3: Optimized mathematical approach using LCM
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

print(lcm_multiple(range(1, 21)))