class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, path, current):
            if current == target:
                res.append(path.copy())
                return
            if index >= len(candidates) or current > target:
                return
            path.append(candidates[index])
            dfs(index + 1, path, current + candidates[index])
            path.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, path, current)

        dfs(0, [], 0)
        return res