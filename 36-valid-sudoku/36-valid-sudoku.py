class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:      
#         box = []
#         for idx in range(len(board)):
#             for num in range(len(board[idx])):
#                 if idx % 3 == 0 and num % 3 == 0:
#                     box.append([board[idx][num], board[idx][num+1], board[idx][num+2], 
#                                 board[idx+1][num], board[idx+1][num+1], board[idx+1][num+2],
#                                 board[idx+2][num],board[idx+2][num+1],board[idx+2][num+2]])
                
#         for idx in range(9):
#             for num in range(9):
#                 if board[idx][num] != '.':
#                     if board[idx] in board[idx][num+1:9]:
#                         return False
                    
#                 if board[num][idx] != '.':
#                     if board[num] in board[num][idx+1:9]:
#                         return False
                 
#                 if box[idx][num] != '.':
#                     if box[idx] in box[idx][num+1:9]:
#                         return False
                
#         return True
    
        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.append(board[i][j])
                     
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    else:
                        col.append(board[j][i])

                if i % 3 == 0 and j % 3 == 0:
                    box = []
                    for k in range(3):
                        k += j
                        for l in range(3):
                            l += i
                            if board[k][l] != '.':
                                if board[k][l] in box:
                                    return False
                                else:
                                    box.append(board[k][l])
        return True
