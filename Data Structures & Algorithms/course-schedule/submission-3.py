class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # tracks courses on the CURRENT path, not total
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return False
            visit.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True



# if processed, we know its good so we can set its prereq to empty