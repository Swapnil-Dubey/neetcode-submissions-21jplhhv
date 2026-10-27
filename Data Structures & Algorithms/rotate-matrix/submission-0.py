class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix)-1

        while l<r:
            for i in range(0,r-l): ###
                top = l
                bottom = r

                topright = matrix[top+i][r] #save top right
                matrix[top+i][r] = matrix[top][l+i] #top right gets top left

                bottomright = matrix[bottom][r-i]
                matrix[bottom][r-i] = topright #bottom right gets top right


                #bottomleft gets bottom right
                bottomleft = matrix[bottom-i][l]
                matrix[bottom-i][l] = bottomright

                #topleft gets bottom left
                matrix[top][l+i] = bottomleft
            r-=1
            l+=1








