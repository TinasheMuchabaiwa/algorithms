'''
PROBLEM DESCRIPTION:

Find the maximum value in a list of integers.
'''

# solution 1 - using recursion
'''The idea is to use recursion to find the maximum value in the list.
    The maximum value is either the first element in the list or the maximum value of the rest of the list. # noqa
'''


def max_value(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] if lst[0] > max_value(lst[1:]) else max_value(lst[1:])


# solution 2 - using a loop
'''The idea is to use a loop to find the maximum value in the list.
    Initialize the maximum value as the first element in the list.
    Iterate over the rest of the list
    update the maximum value if a larger value is found.
'''


def max_value_loop(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


# solution 3 - using memoization
'''The idea is to use memoization to store the maximum value of the list.
    The base case is when the list is empty, return None.
    If the list has only one element, return the element.
    Otherwise, check if the max value is already stored in the memo dict.
    If it is, return the value.
    If it is not, calculate the maximum value and store it in the memo dict.
'''


def max_value_memo(lst, memo={}):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    if tuple(lst) in memo:
        return memo[tuple(lst)]
    memo[tuple(lst)] = max(lst[0], max_value_memo(lst[1:], memo))
    return memo[tuple(lst)]
