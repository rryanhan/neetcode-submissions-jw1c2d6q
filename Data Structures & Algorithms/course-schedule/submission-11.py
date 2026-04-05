class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        completed = set()
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            # to take course, we need pre
            adj[crs].append(pre)  
        
        def dfs(node):
            if node in completed:
                return True
            if node in visiting:
                return False
            visiting.add(node)
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            completed.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# can not return back to a course on the same cycle
# - we add and remove from this set
# once we process a node and backtrack, we can mark it as viewed
# - remove 