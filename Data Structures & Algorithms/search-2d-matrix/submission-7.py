class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input = [[int]] matrix, int target
        #output = true if target exists in matrix
        #constraints: matrix[i] is sorted asc
        #   first int of every row is greater than last int of prev row
        #   O(log(mn)) time : suggests binary search


        # pattern and approach: binary search for the row that target will be a part of, then binary search within that row
        # edge cases: if target doesnt exist in the matrix, then first binary search might not return a result ****
        # time complexity:
        # space complexity: 


        l = 0
        r = len(matrix)-1

        while l<=r:
            mid = (l+r)//2

            if matrix[mid][0]<=target<=matrix[mid][-1]:
                #binary search in this row
                l_row = 0
                r_row = len(matrix[mid])-1

                while l_row<=r_row:
                    mid_row = (l_row+r_row)//2
                    if matrix[mid][mid_row]==target:
                        return True
                    elif matrix[mid][mid_row]>target:
                        r_row = mid_row-1
                    else:
                        l_row = mid_row+1
                # u cant find the thing in the row (even tho row ranges match up)
                return False

            elif matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid+1
        return False
            