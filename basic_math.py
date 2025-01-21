import math

'''
PROBLEM DESCRIPTION:

Generate prime numbers up to a given number.
'''

# solution 1 - brute force (Time complexity: O(n^2))
'''The idea is to iterate over the numbers up to n and for each number,
    check if it is prime by dividing it by all numbers up to its square root.
    If it is prime, add it to the list of prime numbers.
'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


# solution 2 - using the sieve of Eratosthenes (O(n log log n))
'''use the sieve of Eratosthenes algorithm to generate prime numbers up to n.
    Create a list of booleans of size n+1 and initialize all values to True.
    Set the first two values to False since 0 and 1 are not prime.
    Iterate over the numbers up to the square root of n,
    if the number is prime, set all multiples of the number to False.
    Return the indices of the True values in the list.
'''


def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]


# solution 3 - using the optimized sieve of Eratosthenes (O(n log log n))
'''use the sieve of Eratosthenes algorithm to generate prime numbers up to n.
    Create a list of booleans of size n+1 and initialize all values to True.
    Set the first two values to False since 0 and 1 are not prime.
    Iterate over the numbers up to the square root of n,
    if the number is prime, set all multiples of the number to False.
    Return the indices of the True values in the list.
'''


def sieve_of_eratosthenes_optimized(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]


'''
PROBLEM DESCRIPTION:

Find the greatest common divisor (GCD) of two numbers.
'''

# solution 1 - using recursion (Time complexity: O(log(min(a, b))))
'''The idea is to use the Euclidean algorithm to find the GCD of two numbers.
    The base case is when b is 0, return a.
    Otherwise, return the GCD of b and the remainder of a divided by b.
'''


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# solution 2 - using a loop (Time complexity: O(log(min(a, b))))
'''The idea is to use the Euclidean algorithm to find the GCD of two numbers.
    While b is not 0, calculate the remainder of a divided by b,
    set a to b and b to the remainder.
    Return a when b is 0.
'''


def gcd_loop(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# solution 3 - using the math module (Time complexity: O(1))
'''Use the gcd function from the math module to find the GCD of two numbers.
'''


def gcd_math(a, b):
    return math.gcd(a, b)


# solution 4 - using memoization (Time complexity: O(log(min(a, b))))
'''The idea is to use memoization to store the GCD of two numbers.
    The base case is when b is 0, return a.
    If the pair (a, b) is already stored in the memo dict, return the value.
    Otherwise, calculate the GCD of a and b and store it in the memo dict.
'''


def gcd_memo(a, b, memo={}):
    if b == 0:
        return a
    if (a, b) in memo:
        return memo[(a, b)]
    memo[(a, b)] = gcd_memo(b, a % b, memo)
    return memo[(a, b)]


'''
PROBLEM DESCRIPTION:

Find the least common multiple (LCM) of two numbers.
'''

# solution 1 - using the formula (Time complexity: O(1))
'''The idea is to use the formula LCM(a, b) = (a * b) / GCD(a, b)
    to find the least common multiple of two numbers.
'''


def lcm(a, b):
    return (a * b) // gcd(a, b)


# solution 2 - using the math module (Time complexity: O(1))
'''Use the lcm function from the math module to find the LCM of two numbers.
'''


def lcm_math(a, b):
    return abs(a*b) // math.gcd(a, b)


'''
PROBLEM DESCRIPTION:

Find the sum of the digits of a number.
'''

# solution 1 - using recursion (Time complexity: O(log n))
'''The idea is to use recursion to find the sum of the digits of a number.
    The base case is when n is less than 10, return n.
    Otherwise, return sum of the last digit and sum of the rest of the digits.
'''


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


# solution 2 - using a loop (Time complexity: O(log n))
'''The idea is to use a loop to find the sum of the digits of a number.
    Initialize the sum to 0 and iterate over the digits of the number,
    adding each digit to the sum.
    Return the sum.
'''


def sum_of_digits_loop(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# solution 3 - using the math module (Time complexity: O(log n))
'''The idea is to use the sum function from the math module
'''


def sum_of_digits_math(n):
    return sum(int(digit) for digit in str(n))


# solution 4 - using memoization (Time complexity: O(log n))
'''The idea is to use memoization to store the sum of the digits of a number.
    The base case is when n is less than 10, return n.
    If the number is already stored in the memo dict, return the value.
    Otherwise, calculate the sum of the digits and store it in the memo dict.
'''


def sum_of_digits_memo(n, memo={}):
    if n < 10:
        return n
    if n in memo:
        return memo[n]
    memo[n] = n % 10 + sum_of_digits_memo(n // 10, memo)
    return memo[n]


'''
PROBLEM DESCRIPTION:

Find the sum of the first n natural numbers.
'''

# solution 1 - using the formula (Time complexity: O(1))
'''The idea is to use the formula sum = n * (n + 1) / 2
    to find the sum of the first n natural numbers.
'''


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2


# solution 2 - using recursion (Time complexity: O(n))
'''The idea is to use recursion to find the sum of the first n natural numbers.
    The base case is when n is 0, return 0.
    Otherwise, return n plus the sum of the first n-1 natural numbers.
'''


def sum_of_natural_numbers_rec(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers_rec(n - 1)


# solution 3 - using a loop (Time complexity: O(n))
'''The idea is to use a loop to find the sum of the first n natural numbers.
    Initialize the sum to 0 and iterate over the numbers from 1 to n,
    adding each number to the sum.
    Return the sum.
'''


def sum_of_natural_numbers_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


# solution 4 - using memoization (Time complexity: O(n))
'''The idea is to use memoization to store sum of the first n natural numbers.
    The base case is when n is 0, return 0.
    If the number is already stored in the memo dict, return the value.
    Otherwise, calculate the sum of the first n natural numbers,
    store it in the memo dict.
'''


def sum_of_natural_numbers_memo(n, memo={}):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = n + sum_of_natural_numbers_memo(n - 1, memo)
    return memo[n]


'''
PROBLEM DESCRIPTION:

Find the sum of the squares of the first n natural numbers.
'''


# solution 1 - using the formula (Time complexity: O(1))
'''The idea is to use the formula sum = n * (n + 1) * (2n + 1) / 6
    to find the sum of the squares of the first n natural numbers.
'''


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


# solution 2 - using recursion (Time complexity: O(n))
'''idea is to use recursion to find sum of squares of the 1st n natural numbers
    The base case is when n is 0, return 0.
    Otherwise, return the square of n,
    plus the sum of the squares of the first n-1 natural numbers.
'''


def sum_of_squares_rec(n):
    if n == 0:
        return 0
    return n**2 + sum_of_squares_rec(n - 1)


# solution 3 - using a loop (Time complexity: O(n))
'''The idea is to use a loop
    Initialize the sum to 0 and iterate over the numbers from 1 to n,
    adding the square of each number to the sum.
    Return the sum.
'''


def sum_of_squares_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i**2
    return total


# solution 4 - using memoization (Time complexity: O(n))
'''The idea is to use memoization
    The base case is when n is 0, return 0.
    If the number is already stored in the memo dict, return the value.
    Otherwise, calculate the sum of the squares of the first n natural numbers,
    store it in the memo dict.
'''


def sum_of_squares_memo(n, memo={}):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = n**2 + sum_of_squares_memo(n - 1, memo)
    return memo[n]


'''
PROBLEM DESCRIPTION:

Find the sum of the cubes of the first n natural numbers.
'''

# solution 1 - using the formula (Time complexity: O(1))
'''The idea is to use the formula sum = (n * (n + 1) / 2) ^ 2
    to find the sum of the cubes of the first n natural numbers.
'''


def sum_of_cubes(n):
    return (n * (n + 1) // 2) ** 2


# solution 2 - using recursion (Time complexity: O(n))
'''The idea is to use recursion
    The base case is when n is 0, return 0.
    Otherwise, return the cube of n,
    plus the sum of the cubes of the first n-1 natural numbers.
'''


def sum_of_cubes_rec(n):
    if n == 0:
        return 0
    return n**3 + sum_of_cubes_rec(n - 1)


# solution 3 - using a loop (Time complexity: O(n))
'''The idea is to use a loop
    Initialize the sum to 0 and iterate over the numbers from 1 to n,
    adding the cube of each number to the sum.
    Return the sum.
'''


def sum_of_cubes_loop(n):
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total


# solution 4 - using memoization (Time complexity: O(n))
'''The idea is to use memoization
    The base case is when n is 0, return 0.
    If the number is already stored in the memo dict, return the value.
    Otherwise, calculate the sum of the cubes of the first n natural numbers,
    store it in the memo dict.
'''


def sum_of_cubes_memo(n, memo={}):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = n**3 + sum_of_cubes_memo(n - 1, memo)
    return memo[n]
