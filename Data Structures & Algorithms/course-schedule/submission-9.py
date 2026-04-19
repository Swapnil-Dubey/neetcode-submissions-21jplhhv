class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 to numcourses-1

        pre = {}

        for (a,b) in prerequisites:
            if a in pre:
                pre[a].append(b)
            else:
                pre[a] = [b]
        
        #return true if can finish
        def helper(course,visited):
        
            if course in visited:
                return False

            visited.add(course)
            res = True
            if course in pre:
                for i in pre[course]:
                    res = res and helper(i,visited)
            visited.remove(course)
            return res
            


            



        for i in range(numCourses):
            res = helper(i,set())
            if res == False:
                return False
        return True