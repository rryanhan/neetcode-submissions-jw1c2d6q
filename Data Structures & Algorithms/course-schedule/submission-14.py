class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)
        visited = set()
        complete = set()

        def dfs(course):
            if course in complete:
                return True
            if course in visited:
                return False
            visited.add(course)
            for nei in pre[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            complete.add(course)
            return True

    
        for i in range(numCourses):
            if not dfs(i):
                return False
        if len(complete) == numCourses:
            return True
        return False





# if we ever see a cycle, we know it is false
# 
        