# Leetcode 238 – Product of Array Except Self
# Difficulty: Medium
# Tags: Array, Prefix/Suffix Product, Space Optimization

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        lp=[1]*n
        for i in range(1,n):
            lp[i]=lp[i-1]*nums[i-1]
            
        rp=[1]*n
        for i in range(n-2,-1,-1):
            rp[i]=rp[i+1]*nums[i+1]
        
        i=0
        while i < n:
            prod=lp[i]*rp[i]
            res.append(prod)
            i+=1
        return res
        

        