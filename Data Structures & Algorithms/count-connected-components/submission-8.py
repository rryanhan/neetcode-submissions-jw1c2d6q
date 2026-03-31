class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        def find(n1):
            while n1 != parent[n1]:
                parent[n1] = parent[parent[n1]]
                n1 = parent[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # already merged
            if p1 == p2:
                return 0

            # merge p2 into p1
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
            return 1
        for n1, n2 in edges:
            n -= union(n1, n2)
        return n

            
        

# start all nodes separate
# whenever we union, we do n - 1

# union when the parent is different, then merge one into parent of other