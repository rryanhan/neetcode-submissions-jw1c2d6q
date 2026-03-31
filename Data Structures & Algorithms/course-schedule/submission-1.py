class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq =  { i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preReq[course].append(pre)

        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False
            if preReq[course] == []:
                return True

            visitSet.add(course)
            for pre in preReq[course]:
                if not dfs(pre):
                    return False
            preReq[course] = []
            visitSet.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True