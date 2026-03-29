class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input = List[List[int]] matrix, int target
                # Each row in matrix is sorted in non-decreasing order.
                #   matrix[i][0]<matrix[i][1]
                # The first integer of every row is greater than the last integer of the previous row.
                #   matrix[i][0]>matrix[i-1][-1]

        #output = true if target exists in matrix

        #constraints: m == matrix.length
                    # n == matrix[i].length
                    # 1 <= m, n <= 100
                    # -10000 <= matrix[i][j], target <= 10000

        #edge cases: single row, single column
        #pattern: Binary search for row then within row
        #time complexity = O(log(m) + log (n))
        #space complexity = O(1)

        l = 0
        r = len(matrix)-1
        row = -1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row = mid
                break # imp need to break out of this loop once row found
            elif matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid+1
        
        #now we have what row (matrix[row]) target is a part of
        if row == -1:
            return False

        l = 0
        r = len(matrix[row])-1

        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False

