"""
Problem 1: Project Euler

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 1000
result = 0

for i in range(2,n):
    if i%3==0 or i%5==0:
        result += i
print(result)


n = 1000
result = (sum(i for i in range(2,n) if i%3==0 or i%5==0 ))
print(result)