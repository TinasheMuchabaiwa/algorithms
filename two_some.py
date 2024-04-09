"""
PROBLEM DESCRIPTION:

Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

EXAMPLE:

Given nums = [2, 7, 11, 15], target = 9,

"""


# solution 1 - brute force (Time complexity: O(n^2))
'''The idea is to iterate over the list and for each element,
    check if the sum of the element and the next element is equal to the targ.
    If it is, return the indices of the two elements.
'''


def brute_force(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i, j]


# solution 2 - using dictionary (Time complexity: O(n))
'''The idea is to iterate over the list and for each element,
    check if the difference between the target and the element is in the dict.
    If it is, return the indices of the two elements.
    If it is not, add the difference and the index of the element to the dict.
'''


def two_sum(lst, target):
    dic = {}
    for i in range(len(lst)):
        if lst[i] in dic:
            return [dic[lst[i]], i]
        dic[target - lst[i]] = i
