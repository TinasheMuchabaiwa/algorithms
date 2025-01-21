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


# Problem: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# EXAMPLE: nums = [2,7,11,15], target = 9
# OUTPUT: [0,1]
# CONSTRAINTS: 2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9


def twoSum(nums: list[int], target: int):
    # edge cases
    if len(nums) < 2 or len(nums) >= 10**4:
        return []

    if target < -10**9 or target > 10**9:
        return []

    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

    return []


print("TWO SUM: ", twoSum([2, 7, 11, 15], 9))


# Problem: Sorted two sum
# Given an array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
# where 1 <= answer[0] < answer[1] <= numbers.length.
# You may not use the same element twice.
# EXAMPLE: numbers = [2,7,11,15], target = 9
# OUTPUT: [1,2]
# CONSTRAINTS: 2 <= numbers.length <= 3 * 10^4, -1000 <= numbers[i] <= 1000, numbers is sorted in non-decreasing order.


def two_sum_sorted(nums: list[int], target: int):
    # edge cases
    if len(nums) < 2 or len(nums) >= 3 * 10**4:
        return []

    if target < -1000 or target > 1000:
        return []

    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return []


print("TWO SUM SORTED: ", two_sum_sorted([2, 3, 4, 5, 6, 7, 11, 15], 9))


# Problem: Sorted two sum for all pairs
# Given an array of integers numbers that is already sorted in non-decreasing order,
# find all pairs that add up to a specific target number.
# Each pair must be distinct and the pairs must be in ascending order.
# Return a list of lists of size 2, where each list contains the indices of the two numbers.
# The answer list should not contain duplicate pairs.
# EXAMPLE: numbers = [2, 3, 4, 5, 6, 7, 11, 15], target = 9
# OUTPUT: [[0, 1], [2, 3]]


def two_sum_sorted_all_pairs(nums: list[int], target: int):
    # edge cases
    if len(nums) < 2 or len(nums) >= 3 * 10**4:
        return []

    if target < -1000 or target > 1000:
        return []

    left, right = 0, len(nums) - 1
    res = []

    while left < right:
        if nums[left] + nums[right] == target:
            res.append([left, right])
            left += 1
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return res


print("TWO SUM SORTED ALL PAIRS: ", two_sum_sorted_all_pairs([2, 3, 4, 5, 6, 7, 11, 15], 9))
