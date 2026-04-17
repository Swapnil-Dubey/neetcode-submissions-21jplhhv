class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make a dfs functino: cancomplete()

        safe = set()
        #dict that stores course:[listofprereq]
        prereqs = {}
        for i in prerequisites: 
            if i[0] in prereqs:
                prereqs[i[0]].append(i[1])
            else:
                prereqs[i[0]] = [i[1]]
        print(prereqs)
            

        #dfs function that looks at a course and all its prereq and makes sure everyhting can be completed
        # a course can't be completed if there is a cycle(detect using visited)
    
        def cancomplete(course, visited):
            if course in safe:
                return True
            print(course)
            if course in visited:
                return False
            
            visited.add(course)
            res = True
            if course in prereqs:
                for prereq in prereqs[course]:
                    res = res and cancomplete(prereq, visited)
            visited.remove(course)
            if res == True:
                safe.add(course)
            return res


        
        for i in range(numCourses):
            res = cancomplete(i, set())
            if res == False:
                return False
        return True