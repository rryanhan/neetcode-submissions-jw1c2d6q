class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        visit = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
        
            length = r - l + 1
            res = max(res, length)
        return res
            
# x y z x y z
#

        





# res variable 
# use a set

# l, r pointers
# while s[r] in set:
# -> increment l by 1

# len()