class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {}
        
        for p in prerequisites: 
            if p[0] in pre:
                pre[p[0]].append(p[1])
            else:
                pre[p[0]] = [p[1]]
        # {A:[B,C]}
        res = []
        visited = set()

        def dfs(i):
            if i in visited:
                return False

            if i in pre:
                visited.add(i)
                for req in pre[i]:
                    ret = dfs(req)
                    if ret == False:
                        return False
                visited.remove(i)
            if i not in res:
                res.append(i)
            return True
        for i in range(numCourses):
            if i in res:
                continue
            ret = dfs(i)
            if ret == False:
                return []
        return res
            

