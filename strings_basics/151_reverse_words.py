# Leetcode 151 - Reverse Words in a String
# Difficulty: Medium
# Tags: Strings, Two Pointers


class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        rev_words=words[::-1]
        new_str=[]
        for word in rev_words:
            if word:

                new_str.append(word)
        return ' '.join(new_str)
            

        