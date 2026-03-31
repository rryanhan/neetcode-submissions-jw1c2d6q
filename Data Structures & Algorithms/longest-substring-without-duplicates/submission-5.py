class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupSet = set()
        res = 0
        left = 0

        for i in range(len(s)):
            while s[i] in dupSet:
                dupSet.remove(s[left])
                left += 1
            dupSet.add(s[i])
            res = max(res, i - left + 1)
        return res
