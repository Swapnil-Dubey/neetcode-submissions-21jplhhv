class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix)-1

        row = -1 #not false bcz 0 might be false
        while u<=d:
            mid = (u+d)//2# = 1

            if target >= matrix[mid][0] and target<= matrix[mid][-1]:
                row = mid
                break # dont forget to break here after u find the correct row otherwise u inf loop
            elif target>matrix[mid][-1]:
                u = mid+1
            else:
                d=mid-1
        
        
        
        if row == -1:
            return False
        l = 0
        r = len(matrix[row])-1
        while l<=r: #= bcz what if it a 1 col matrix
            mid = (l+r)//2

            if matrix[row][mid] == target:
                return True
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                r=mid-1
        


        return False
