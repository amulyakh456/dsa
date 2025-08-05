# Leetcode 1672 - Richest Customer Wealth
# Difficulty: Easy
# Tags: Arrays, Matrix


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        money=[]
        m=len(accounts)
        for i in range(m):
            n=len(accounts[i])
            w=0
            for j in range(n):
                w+=accounts[i][j]
            money.append(w)
        return max(money)

        