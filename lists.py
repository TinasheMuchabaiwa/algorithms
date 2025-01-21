# input - sorted array (non-decreasing) (nums)
# task - remove duplicates in-place. (Can't Create new array)
# output - Number of unique elements (k) AND modify array.
# constraints - First k elements of nums should be unique and in original order.

def rem_duplicates(nums):
    if not nums:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k


print(rem_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))


# Problem:
# Given an array nums, move all zeros to the end while maintaining the relative order of the non-zero elements.
# Modify the array in-place and return the modified array.
# Input: nums (not sorted) eg - [0,1,0,3,12]
# Output: [1,3,12,0,0]. No reordering of non-zero elements.
# Constraints: Modify the array in-place. Do not allocate extra space.
# edge cases: nums is empty, nums has only one element, nums has all zeros, nums has no zeros.

def move_zeros(nums):
    if not nums:
        return []

    non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1

    return nums


print("ZEROS: ", move_zeros([0, 1, 0, 3, 12]))


# Problem: Given an integer array nums and an integer val, remove all occurrences of val in-place
# and return the new length.
# The relative order of the elements may be changed.
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Constraints: Modify the array in-place. Do not allocate extra space.
# edge cases: nums is empty, nums has only one element, nums has all zeros, nums has no zeros.

def remove_element(nums, val):
    if not nums:
        return 0

    if len(nums) == 1:
        return 0 if nums[0] == val else 1

    for i in nums:
        if i == val:
            nums.remove(i)
    return len(nums)


print("REMOVE: ", remove_element([3, 2, 2, 3], 3))


# Problem: Given an array, rotate the array to the right by k steps, where k is non-negative.
# You must do this in-place.
# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: [4,5,6,7,1,2,3]
# Constraints: Modify the array in-place. Do not allocate extra space.

def rotate_array(nums, k):
    if not nums:
        return []

    if k == 0 or k == len(nums) or len(nums) == 1:
        return nums

    nums = nums[-k:] + nums[:k]
    return nums


print("ROTATE: ", rotate_array([1, 2, 3, 4, 5, 6, 7], 4))


# Problem: Given an unsorted integer array nums, find the smallest missing positive integer.
# You must solve the problem in O(n) time and in constant space.
# Input: nums = [3, 4, -1, 1]
# Output: 2

def first_missing_positive(nums):
    if not nums:
        return 1

    nums = set(nums)

    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


print("MISSING: ", first_missing_positive([3, 4, -1, 1]))


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


# Problem: 3-SUM - Given an integer array nums,return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums: list[int]):
    if len(nums) < 3:
        return []

    nums.sort()

    result = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            # [-4, -2, -1, 1, 2, 3, 4]
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1

            else:
                right -= 1
    return result


print("THREE SUM: ", threeSum([-1, 0, 1, 2, -1, -4]))
