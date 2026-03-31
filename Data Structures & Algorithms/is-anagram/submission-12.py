class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrayOfC = [0] * 26
        for i in range(len(s)):
            arrayOfC[ord(s[i]) - ord('a')] += 1
            arrayOfC[ord(t[i])- ord('a')] -= 1
        for i in arrayOfC:
            if i != 0:
                return False
        return True