class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(index):
            # base case
            if index == len(nums):
                res.append(path.copy())
                return

            # option 1: add
            path.append(nums[index])
            dfs(index + 1)
            path.pop()
            # option 2: dont add
            dfs(index + 1)

        dfs(0)
        return res



# we either add, or we dont
        