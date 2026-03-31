class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLength = 0
        for i in range(len(nums)):
            if i > maxLength:
                return False
            maxLength = max(maxLength, i + nums[i])
        return True

        

# always extend to the farthest reachable position
# if current index is ever less than the farthest reachable, return false

# [ 1, 2, 0, 1, 0]
# i = 0
# - max reachable is index 1
# i = 1
# - max reachable index is index 3
# i = 2
# - max reachable index is 3
# i = 3
# - max reachable index is 4, so it is true