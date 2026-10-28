class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix)-1


        while l<r:
            top = l#isince its a square
            bottom = r

            for i in range(r-l): #impp remember

                #top right stored
                topright = matrix[top+i][r]
                #top left goes to topright
                matrix[top+i][r] = matrix[top][l+i]


                #bottom right stored
                bottomright = matrix[bottom][r-i]
                #top right goes to bottomright
                matrix[bottom][r-i] = topright


                #bottom left stored
                bottomleft = matrix[bottom-i][l]
                #bottom right goes to bottom left
                matrix[bottom-i][l] = bottomright


            
                #bottom left goes to top left
                matrix[top][l+i] = bottomleft

            l+=1 #works because top and bottom is bounded by l and r
            r-=1


        