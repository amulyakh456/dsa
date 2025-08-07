# Leetcode 66 – Plus One
# Difficulty: Easy
# Tags: Array, Simulation, Carry

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        snum="".join(str(num) for num in digits)
        inum=int(snum)
        inum+=1
        ans=[int(num) for num in str(inum)]
        return ans
        


