# Leetcode 345 - Reverse Vowels of a String
# Difficulty: Easy
# Tags: Strings, Two Pointers


class Solution:
    def reverseVowels(self, s: str) -> str:
        str_lower=s.lower()
        vowels=['a','e','i','o','u']
        vowels_str=[]
        length=len(s)
        new_str=''
        for i in s:
            if i.lower() in vowels:
                vowels_str.append(i)
        num_v=len(vowels_str)
        
        for j in range(len(str_lower)):
            if str_lower[j] in vowels:
                new_str+=vowels_str[-1]
                vowels_str.pop(-1)
            else:
                new_str+=s[j]
        return new_str

        