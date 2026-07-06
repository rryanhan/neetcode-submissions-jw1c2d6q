class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tracker = [False] * len(nums)
        res = []
        path = []

        def dfs(index):
            # base case
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):

                if tracker[i] == True:
                    continue
                
                # dive deeper
                tracker[i] = True
                path.append(nums[i])
                dfs(i)

                # backtracker
                tracker[i] = False
                path.pop()


        dfs(0)
        return res
        


# we can keep tr
# what is index vs i?
# 

