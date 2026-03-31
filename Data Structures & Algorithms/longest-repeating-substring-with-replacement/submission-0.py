class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxF = 0
        res = 0

        for c in range(len(s)):
            count[s[c]] = count.get(s[c], 0) + 1
            
            maxF = max(maxF, count[s[c]])

            while (c - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(c - l + 1, res)
        return res
                
        