class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        candidates.sort()

        def dfs(index, sumPath):
            if sumPath == target:
                res.append(path.copy())
                return
                
            if sumPath > target or index == len(candidates):
                return
 
            
            path.append(candidates[index])
            dfs(index + 1, sumPath + candidates[index])
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
                
            path.pop()
            dfs(index + 1, sumPath)
        dfs(0, 0)
        return res

        
        




        # move on ->
            # take or skip the number 