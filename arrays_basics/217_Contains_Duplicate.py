class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr=list(set(nums))
        if len(arr)!=len(nums):
            return True
        return False