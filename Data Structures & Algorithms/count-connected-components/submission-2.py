class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find (n2)
            if p1 == p2:
                return 0
            if size[p1] > size[p2]:
                parent[p2] = parent[p1]
                size[p1] += size[p2]
            else: 
                parent[p1] = parent[p2]
                size[p2] += size[p1]
            return 1
        res = n
        for node1, node2 in edges:
            res -= union(node1, node2)
        return res




