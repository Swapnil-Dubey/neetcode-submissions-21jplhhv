class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search for row

        l = 0
        r = len(matrix)-1
        row = -1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row = mid
                break # dont forget to break out of this loop once you found the row
            elif target<matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
            
        if row == -1:
            return False



        #binary search for value within row    

        l = 0
        r = len(matrix[row])-1

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l=mid+1
        return False 