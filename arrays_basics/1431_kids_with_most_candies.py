# Leetcode 1431 - Kids With the Greatest Number of Candies
# Difficulty: Easy
# Tags: Arrays

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        newarr = []
        for i in range(len(candies)):
            max = candies[i] + extraCandies
            na = candies[:]
            count = True
            na[i] = max
            
            for j in na:

                if j>max:
                    count = False
                    break
            newarr.append(count)
            
        return newarr