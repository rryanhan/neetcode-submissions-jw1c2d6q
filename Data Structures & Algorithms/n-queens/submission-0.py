class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        topRight = set() #[r + c]
        botRight = set()#[r - c]
        res = []
        path = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                validGraph = []
                for row in path:
                    listToMerge = "".join(row)
                    validGraph.append(listToMerge)
                res.append(validGraph)
                return
            
            for c in range(n):
                if c in col or (r + c) in topRight or (r - c) in botRight:
                    continue
                
                col.add(c) 
                topRight.add(r + c)
                botRight.add(r - c) 
                path[r][c] = "Q"


                dfs(r + 1)

                col.remove(c) 
                topRight.remove(r + c)
                botRight.remove(r - c) 
                path[r][c] = "."
            return
            

        dfs(0)
        return res