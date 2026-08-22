class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n

        for row in range(m - 2, -1, -1):
            newRow = [1] * n
            for col in range(n - 2, -1, -1):
                newRow[col] = newRow[col + 1] + res[col]
            res = newRow

        return res[0]


        