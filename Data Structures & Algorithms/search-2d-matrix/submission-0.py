class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            l, r = 0, len(n) - 1
            while l <= r:
                tar = (r + l) // 2
                if n[tar] > target:
                    r = tar - 1
                elif n[tar] < target:
                    l = tar + 1
                else:
                    return True
        return False

