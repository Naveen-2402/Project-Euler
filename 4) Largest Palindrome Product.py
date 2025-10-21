"""
Problem 4: Project Euler

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

max_factor = 999
min_factor = 100

def largest_palindrome():
    factor_a, factor_b, max_palindrome = 0, 0, 0
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                factor_a, factor_b, max_palindrome = i, j, product
    return max_palindrome, factor_a, factor_b

print(largest_palindrome())


# Approch 2:

print(max((i*j, i, j) for i in range(999, 100, -1) for j in range(i, 100, -1) if str(i * j) == str(i * j)[::-1]))