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
