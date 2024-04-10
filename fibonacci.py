"""
PROBLEM DESCRIPTION:

Use the Fibonacci sequence to find the nth number in the sequence.
"""

# solution 1 - using recursion (Time complexity: O(2^n))
'''The idea is to use recursion to find the nth number in the sequence.
    The base case is when n is 0 or 1, return n.
    Otherwise, return the sum of the previous two numbers in the sequence.
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# solution 2 - using memoization (Time complexity: O(n))
'''The idea is to use memoization to store the values of the sequence.
    The base case is when n is 0 or 1, return n.
    Otherwise, check if the value of n is already stored in the memo dict.
    If it is, return the value.
    If it is not, calculate the value and store it in the memo dict.
'''


def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
