# Leetcode 53 – Maximum Subarray
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Kadane’s Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=current_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_sum=max(current_sum,max_sum)
        return max_sum
