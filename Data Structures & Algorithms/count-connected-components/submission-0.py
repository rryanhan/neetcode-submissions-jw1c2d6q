class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        visit = set()
        res = 0

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        def dfs(node):
            for neighbors in adj[node]:
                if neighbors not in visit:
                    visit.add(neighbors)
                    dfs(neighbors)

        for i in range(n):
            if i not in visit:
                visit.add(i)
                res += 1
                dfs(i)
        return res


        