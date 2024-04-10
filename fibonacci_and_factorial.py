import timeit

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


'''
PROBLEM DESCRIPTION:

Use the factorial function to find the factorial of a number.
'''

# solution 1 - using recursion (Time complexity: O(n))
'''The idea is to use recursion to find the factorial of a number.
    The base case is when n is 0 or 1, return 1.
    Otherwise, return the product of n and the factorial of n-1.
'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    return n*factorial(n-1)


# solution 2 - using memoization (Time complexity: O(n))
'''The idea is to use memoization to store the values of the factorial.
    The base case is when n is 0 or 1, return 1.
    Otherwise, check if the value of n is already stored in the memo dict.
    If it is, return the value.
    If it is not, calculate the value and store it in the memo dict.
'''


def factorial_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    memo[n] = n*factorial_memo(n-1, memo)
    return memo[n]


print({
    "factorial_of_50": factorial(50),
    "factorial_time_taken": timeit.timeit(lambda: factorial(50), number=1000),
    "factorial_of_50_memo": factorial_memo(50),
    "factorial_memo_time_taken": timeit.timeit(
        lambda: factorial_memo(50), number=1000
    ),
})
