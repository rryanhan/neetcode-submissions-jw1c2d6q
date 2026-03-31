class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        # while r isnt last index - stop if last index
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res


        
        

# Greedy solution       
# per i, take the index we can jump the furthest with
# BFS: indices that can be hit in i jumps
# - how do we expand i?

# take the max you can jump in i, use that as bound for i + 1
#[ 2, 4, 1, 1, 1, 1]

# 0 jumps: start at 2 - take 2 as max
# 1 jump: can cover 2, 4, 1 - take 4 as max
# 2 jump: starts at 4 as it is the max, cover the rest
