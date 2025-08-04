# Leetcode 1768 - Merge Strings Alternately
# Difficulty: Easy
# Tags: Strings, Simulation


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_str=""
        len1=len(word1)
        len2=len(word2)
        if len1>len2:
            for i in range(len2):
                new_str+=word1[i]
                new_str+=word2[i]
            new_str+=word1[i+1:]
        else:
            for j in range(len1):
                new_str+=word1[j]
                new_str+=word2[j]
            new_str+=word2[j+1:]
        return new_str