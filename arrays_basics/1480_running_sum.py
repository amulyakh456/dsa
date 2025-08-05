# Leetcode 1480 - Running Sum of 1D Array
# Difficulty: Easy
# Tags: Arrays, Prefix Sum



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        runningSum.append(nums[0])
        i=1
        while i<len(nums):
            summ=runningSum[i-1]
            summ+=nums[i]
            runningSum.append(summ)
            i+=1

        return runningSum
        