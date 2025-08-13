class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=0
        white=0
        blue=0

        for i in nums:
            if i==0:
                red+=1
            elif i==1:
                white+=1
            elif i==2:
                blue+=1
        i=0
        j=0
        k=0
        l=0
        while i<red:
            nums[l]=0
            i+=1
            l+=1

        while j<white:
            nums[l]=1
            j+=1
            l+=1

        while k<blue:
            nums[l]=2
            k+=1
            l+=1
        