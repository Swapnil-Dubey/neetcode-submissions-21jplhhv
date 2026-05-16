class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}

        for a,b in prerequisites:
            if a in pre:
                pre[a].append(b)
            else:
                pre[a] = [b]
        

        #returns true if u can take this course without cycles
        def dfs(i):
            if i in visited:
                return False
            if i not in pre:
                return True
            visited.add(i)
            
            for prereq in pre[i]:
                ret = dfs(prereq)
                if ret == False:
                    return False
            visited.remove(i)
            return True




        for i in range(numCourses):
            visited = set()
            ret = dfs(i)
            if ret == False:
                return False
        return True
        