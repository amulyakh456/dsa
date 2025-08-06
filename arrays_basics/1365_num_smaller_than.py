# Leetcode 1365 – How Many Numbers Are Smaller Than the Current Number
# Difficulty: Easy
# Tags: Arrays, Counting



class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]>nums[j]:
                        c+=1
            count.append(c)
        return count
        