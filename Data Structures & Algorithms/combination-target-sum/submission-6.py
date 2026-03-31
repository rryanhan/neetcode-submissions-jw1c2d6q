class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        tracker = []
        def dfs(index, summation):
            if summation == target:
                res.append(tracker.copy())
                return
            if summation > target or index >= len(nums):
                return
            tracker.append(nums[index])
            dfs(index, summation + nums[index])
            tracker.remove(nums[index])
            dfs(index + 1, summation)


        dfs(0, 0)
        return res