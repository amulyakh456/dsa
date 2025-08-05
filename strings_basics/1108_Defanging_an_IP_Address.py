# Leetcode 1108 - Defanging an IP Address
# Difficulty: Easy
# Tags: Strings

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged=""
        for i in range(len(address)):
            if address[i]==".":
                defanged+="[.]"
            else:
                defanged+=address[i]
        return defanged

        