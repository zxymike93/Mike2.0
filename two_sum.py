"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class MySolution:
    def two_sum3(self, nums, target):
        lookup = {}
        for i, x in enumerate(nums):
            if target - x in nums:
                return lookup[target-x], i
            lookup[x] = i
        return []

    def two_sum1(self, nums, target):
        for i in nums:
            j = target - i
            if j in nums:
                if j != i:
                    return nums.index(i), nums.index(j)
                else:
                    try:
                        index_i = nums.index(i)
                        index_j = nums.index(j, index_i+1)
                    except ValueError:
                        pass
                    else:
                        return index_i, index_j

    def two_sum2(self, nums, target):
        for i, x in enumerate(nums):
            y = target - x
            index_y = nums.find(y)
            if index_y > i:
                return i, index_y
