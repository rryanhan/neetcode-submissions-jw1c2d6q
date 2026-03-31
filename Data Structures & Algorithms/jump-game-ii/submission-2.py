class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, res = 0, 0, 0

        # as long as it is not the last index
        while r < len(nums) - 1:
            
            localMax = 0
            for i in range(l, r + 1):
                localMax = max(localMax, i + nums[i])
            l = r + 1
            r = localMax
            res += 1
        return res

#greedy: make best local decision right now
# step 1: l pointer, r pointer
# step 2: for numbers in l to r:
#         calculate biggest jump
# step 3: new l becomes r + 1
#         new r becomes biggest jump
# step 4: increment res by 1