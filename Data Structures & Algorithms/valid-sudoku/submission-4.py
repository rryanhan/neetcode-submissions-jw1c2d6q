class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cSet = [set() for i in range(9)]
        rSet = [set() for i in range(9)]
        bSet = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                box = (r//3) * 3 + (c//3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in cSet[c]:
                    return False
                else:
                    cSet[c].add(board[r][c])
                
                if board[r][c] in rSet[r]:
                    return False
                else: 
                     rSet[r].add(board[r][c])

                if board[r][c] in bSet[box]:
                    return False
                else:
                    bSet[box].add(board[r][c])
        return True

# r // 3 + c // 3

 #       c = 4, r = 2 is box 2