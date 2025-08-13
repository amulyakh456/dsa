class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        i=0
        j=l-1
        
        while i<=j:
            if nums[i]==val:
                nums[i]=nums[j]
                j-=1
                
            else:
                i+=1
        return i
            
           