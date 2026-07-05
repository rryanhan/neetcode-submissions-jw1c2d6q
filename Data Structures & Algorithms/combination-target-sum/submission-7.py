class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        
        def dfs(index, curr):
            if curr > target or index == len(nums):
                return
            
            if curr == target:
                res.append(path.copy())
                return
            # keep same number
            path.append(nums[index])
            dfs(index, curr + nums[index])

            # move to next number
            path.remove(nums[index])
            dfs(index + 1, curr)
        dfs(0, 0)

        return res

        
        # take current number and stay index
        # skip the number and move to the next index

        # base case: 
        #   - if combination sums up to 9, append to res
        #   - if index == len(nums), return

        # 2 options:
        #   - keep same number
        #   - move onto next number