# Leetcode 167 – Two Sum II (Input Array is Sorted)
# Difficulty: Medium
# Tags: Two Pointers, Array, Sorted Array


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while right>left:
            cur_sum=numbers[left]+numbers[right]
            if cur_sum==target:
                return [left+1,right+1]
            elif cur_sum<target:
                left+=1
            else:
                right-=1