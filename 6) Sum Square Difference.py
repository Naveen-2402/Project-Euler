"""
Problem 6: Project Euler

The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


# Approach 1: Using Reducer
from functools import reduce
list_100 = list(range(1,101))

def add(a,b):
    return a + b

def square(a,b):
    return a + b*b

sum_sqr = reduce(add,list_100)
sum_sqr *= sum_sqr 
sqr_sum = reduce(square,list_100,0)
print(f"{sum_sqr-sqr_sum=}")



# Approach 2: Using Generator expression
sum_square = sum(range(1,101))**2
square_sum = sum(i*i for i in range(1,101))
print(f"{sum_square-square_sum=}")