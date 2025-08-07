# Leetcode 1512 – Number of Good Pairs
# Difficulty: Easy
# Tags: Array, HashMap, Counting



class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j]:
                    count+=1
        return count
                    

                