class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()

        def dfs(index):
            if index >= len(nums):
                res.append(path.copy())
                return
            
            # choice 1: take the number
            path.append(nums[index])
            dfs(index + 1)

            # choice 2: skip the number
            #   - this means we skip all duplicates
            path.pop()
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            index += 1
            dfs(index)

        dfs(0)
        return res
            