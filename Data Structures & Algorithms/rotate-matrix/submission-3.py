class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

# top left goes by row, column static
# bottom left goes by column, row static
# bottom right goes by row, column static
# top right goes by column, row static

# top, bottom are rows |  l, r are cols
                # topLeft
                topLeft = matrix[top][l + i]

                # topLeft with bottom left
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom left with bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #bottom right with top right
                matrix[bottom][r - i] = matrix[top + i][r]

                # top right with top left
                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1

# a b c d   # m i e a
# e f g h   # n j f b
# i j k l   # o k g c
# m n o p   # p l h d


        