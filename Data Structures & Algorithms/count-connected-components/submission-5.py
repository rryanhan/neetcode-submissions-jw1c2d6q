class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n

        # find the parent node 
        def find(node):
            res = node
            while res != parent[res]:
                res = parent[res]
            return res
    
        # find parent nodes. if they are the same, they are merged already
        # if they are differnt, merge the smaller one into larger one
        # subtract n by 1
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if size[p1] >= size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1] 
            return 1       
        for e1, e2 in edges:
            n -= union(e1, e2)
        return n
        