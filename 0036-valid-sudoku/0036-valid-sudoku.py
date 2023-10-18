class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            lst = []
            for j in range(9):
                if board[i][j] in lst and board[i][j] != ".":
                    return False
                else:
                    lst += board[i][j]


        for i in range(9):
            lst = []
            for j in range(9):
                if board[j][i] in lst and board[j][i] != ".":
                    return False
                else:
                    lst += board[j][i]
            print(lst)
        
        boxes = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                # every 3 rows, every 3 columns
                boxes.append([row[j:j+3] for row in board[i:i+3]])
        
        for b in boxes:
            cum = (sum(b,[]))
            lst = []
            for i in range(9):
                if cum[i] in lst and cum[i] != ".":
                    return False
                lst += [cum[i]]

        
        return True
        
            
