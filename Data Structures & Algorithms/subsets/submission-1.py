class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def dfs(index):
            if index >= len(nums):
                res.append(path.copy())
                return

            path.append(nums[index])
            dfs(index + 1)
            path.remove(nums[index])
            dfs(index + 1)
        dfs(0)
        return res





        # base case: index >= len(nums)
        #   - if so, get copy of the list and add it to res

        # else:
        #   - add number to list, run dfs, pop to backtrack

        