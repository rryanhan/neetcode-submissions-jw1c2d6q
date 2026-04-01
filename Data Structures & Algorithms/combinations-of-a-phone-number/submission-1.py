class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def dfs(index, string):
            if index >= len(digits):
                res.append(string)
                return
            for char in dic[digits[index]]:
                dfs(index + 1, string + char)
            
        dfs(0, "")

        return res if digits else []

        
        