class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        # SETS ARE UNORDERED, NEED A RES ARRAY
        res = []
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            # to take course, we need pre
            adj[crs].append(pre)  
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res