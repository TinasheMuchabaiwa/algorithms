'''
PROBLEM DESCRIPTION:

Search for a value in a list of integers.
'''

# solution 1 - using linear search
'''The idea is to use linear search to find the value in the list.
    Iterate over the list and check if the value is equal to the target.
    If it is, return the index of the value.
    If the value is not found, return -1.
'''


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# solution 2 - using binary search
'''The idea is to use binary search to find the value in the list.
    Initialize left & right pointers as the first and last indices of the list.
    While the left pointer is less than or equal to the right pointer,
    calculate the middle index,
    check if the value at the middle index is equal to the target.
    If it is, return the middle index.
    If the target is less than the value at the middle index,
    update the right pointer to mid - 1.
    If the target is greater than the value at the middle index,
    update the left pointer to mid + 1.
    If the value is not found, return -1.
'''


def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# solution 3 - using recursion
'''The idea is to use recursion to search for the value in the list.
    The base case is when the list is empty, return -1.
    If the first element of the list is equal to the target, return 0.
    Otherwise, search for the target in the rest of the list.
    If the target is found, return the index + 1.
    If the target is not found, return -1.
'''


def search_rec(lst, target):
    if not lst:
        return -1
    if lst[0] == target:
        return 0
    res = search_rec(lst[1:], target)
    return -1 if res == -1 else res + 1


# solution 4 - using memoization
'''The idea is to use memoization to store the index of the value in the list.
    The base case is when the list is empty, return -1.
    If the target is already stored in the memo dict, return the value.
    If the target is not found, return -1.
    If the target is found, calculate the index and store it in the memo dict.
'''


def search_memo(lst, target, memo={}):
    if not lst:
        return -1
    if target in memo:
        return memo[target]
    if lst[0] == target:
        memo[target] = 0
        return memo[target]
    res = search_memo(lst[1:], target, memo)
    memo[target] = -1 if res == -1 else res + 1
    return memo[target]
