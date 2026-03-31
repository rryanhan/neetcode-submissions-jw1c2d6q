class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS, newT = sorted(s), sorted(t)
        return newS == newT