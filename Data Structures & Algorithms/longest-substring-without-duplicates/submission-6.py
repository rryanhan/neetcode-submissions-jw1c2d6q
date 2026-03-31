class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        

# maxL
# if r != l, move right one, maxL += 1
# if r = l, move left over one
#   maxL -=1
# when right > len(s), end, add return maxL
#   z     x     y       z        x        y       z
#   l.          r
#
#    x     x       x       x       x
#.                                  l     r
#
#
#
#

