class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sNums = set(nums)
        res = 0
        for n in sNums:
            if (n-1) in sNums:
                continue
            cur = 0
            while (n + cur) in sNums:
                cur += 1
            res = max(cur, res)
        return res
            
        