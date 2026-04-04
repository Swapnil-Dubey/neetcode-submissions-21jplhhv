class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #input: prerequisites array: prerequisites[i] = [a,b] to take a u need to take b first, numcourses
        #output: ordering of range(numcourses) that satisfy prerequisites
        #constraints: 1 <= numCourses <= 1000
        #               0 <= prerequisites.length <= 1000
        #               All prerequisite pairs are unique.
        #pattern: Graphs
        #approach: 
        #edge cases:
        #time complexity:
        #space complexity: 

        #prereq map

        prereq = {}
        for (a,b) in prerequisites:
            if a in prereq:
                prereq[a].append(b)
            else:
                prereq[a] = [b]
        res = []
        visited = set()
        print(prereq)

        # prereq ={1:[0]}
        def dfs(i):
            nonlocal res
            nonlocal prereq
            if i in visited:
                return False
            if i in prereq:
                visited.add(i)
                for req in prereq[i]:
                    ret = dfs(req)
                    if ret == False:
                        return False
                    
                visited.remove(i)
            if i not in res:
                res.append(i)

        for i in range(numCourses):
            if i in res:
                continue
            ret = dfs(i)
            if ret == False:
                return []
        return res

        

        



