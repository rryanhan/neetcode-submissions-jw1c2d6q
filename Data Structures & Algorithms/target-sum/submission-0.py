class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(index, curr):
            if index == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            return dfs(index + 1, curr + nums[index]) + dfs(index + 1, curr - nums[index])


        return dfs(0, 0)