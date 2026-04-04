class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #input: prerequisites[i] = [a, b]: must take course b to take course a
        #       , numcourses : number of courses required to take from 0 to numcourses-1
        #output = True if possible to finish all courses
        #Pattern: graphs (cycle detection)
        #approach: create map of course num to list of reqd courses then run dfs, along with visited set at each numcourse
        #time complexity: 
        #space complexity: 

        prereqmap = {}
        visited = set()

        for i in prerequisites:
            if i[0] in prereqmap:
                prereqmap[i[0]].append(i[1])
            else:
                prereqmap[i[0]] = [i[1]]
        print(prereqmap)

        def dfs(i,seeninthisdfs):
            
            if i in prereqmap:
                for prereq in prereqmap[i]:
                    if prereq in seeninthisdfs: 
                        return False
                    if prereq in visited:
                        continue
                    seeninthisdfs.append(prereq)
                    if not dfs(prereq, seeninthisdfs):
                        return False
                    seeninthisdfs.pop(-1)
                

            return True
            
            



        #{0:[1]}
        
        for i in range(numCourses):
            resofi = dfs(i, [])
            if resofi == False:
                return False
            visited.add(i)

        return True
