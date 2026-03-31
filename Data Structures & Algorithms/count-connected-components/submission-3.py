class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {i : [] for i in range(n)}
        visited = set()
        res = 0

        for nOne, nTwo in edges:
            dic[nOne].append(nTwo)
            dic[nTwo].append(nOne)

        def dfs(node):
            for children in dic[node]:
                if children not in visited:
                    visited.add(children)
                    dfs(children)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        return res

