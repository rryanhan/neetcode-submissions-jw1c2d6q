class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.alphaNumeric(s[l]) and l < r:
                l += 1
            while not self.alphaNumeric (s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNumeric(self, char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9' 


# "Was it a car or a cat I saw?"
#. l   
# "Was it a car or a cat I saw?" 
#. l                         r
# 
#
#
#
#
#
#

        