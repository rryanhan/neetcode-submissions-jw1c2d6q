class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opening, closing, path):
            if closing > opening or opening > n:
                return
            if ((opening + closing) == n * 2) and (opening == closing):
                res.append(path)
                return
            
            # opening bracket
            dfs(opening + 1, closing, path + "(")
            print(path)

            # closing bracket
            dfs(opening, closing + 1, path + ")")
        
        dfs(0, 0, "")
        return res
