# Leetcode 136 – Single Number
# Difficulty: Easy
# Tags: Arrays, Bit Manipulation


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[0:i]+nums[i+1:]
            if nums[i] not in n:
                return nums[i]