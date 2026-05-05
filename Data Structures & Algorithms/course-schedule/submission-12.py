class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}


        for (a,b) in prerequisites:
            if a in prereqs:
                prereqs[a].append(b)
            else:
                prereqs[a] = [b]
        #{0:[1]}
        
        #returns true if can take course(no cycles in its prereq tree)
        
        def canTake(course):
            if course in visited:
                return False

            if course not in prereqs:
                return True


            visited.add(course)
            

            res = True
            for pre in prereqs[course]:
                res = res and canTake(pre)
            
            visited.remove(course)
            prereqs[course] = []
            return res

        for i in range(numCourses):
            visited = set()
            res = canTake(i)
            if res == False:
                return False
        return True
