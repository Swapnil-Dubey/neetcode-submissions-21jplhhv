class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #each row is in ASC order
        # first in of row is greater than last int of prev row(essentially left to right up to down increasing order)

        #first search for the row this target should be a part of, then search within that row


        l = 0
        r = len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                #search within this row
                l_row = 0
                r_row = len(matrix[mid])-1
                while l_row<=r_row:
                    mid_row = (l_row+r_row)//2
                    if matrix[mid][mid_row] == target:
                        return True
                    elif matrix[mid][mid_row]<target:
                        l_row = mid_row+1
                    else:
                        r_row = mid_row-1
                return False
                

            elif target<matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        return False
            