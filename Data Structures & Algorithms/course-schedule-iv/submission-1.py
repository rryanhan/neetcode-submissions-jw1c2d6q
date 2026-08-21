class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        linked = {}

        for pre, course in prerequisites:
            adj[course].append(pre)
        visiting = set()
        
        def dfs(course):

            if course in linked:
                return linked[course]
            linked[course] = set()

            for nei in adj[course]:
                linked[course] |= dfs(nei)
            
            linked[course].add(course)
            return linked[course]


            

        for num in range(numCourses):
            dfs(num)
        
        return [uj in linked[vj] for uj, vj in queries]
