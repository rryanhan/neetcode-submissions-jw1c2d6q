class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i : [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return True if (dfs(0, -1) and len(visit) == n) or not n else False
        
        