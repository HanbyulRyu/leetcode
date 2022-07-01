from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board[0])
        col = len(board)
        prev = deepcopy(board)
        # print(prev)
        
        for i in range(col):
            for j in range(row):
                lives = 0
                # 윗줄 3개 체크
                if i > 0:
                    if j > 0 and prev[i-1][j-1]:
                        lives += 1
                    if prev[i-1][j]:
                        lives += 1
                    if j < row-1 and prev[i-1][j+1]:
                        lives += 1
                # 양옆
                if j > 0 and prev[i][j-1]:
                    lives += 1
                if j < row-1 and prev[i][j+1]:
                    lives += 1
                # 아랫줄
                if i < col-1:
                    if j > 0 and prev[i+1][j-1]:
                        lives += 1
                    if prev[i+1][j]:
                        lives += 1
                    if j < row-1 and prev[i+1][j+1]:
                        lives += 1
                        
                # print(i, j, ":", lives)
                
                if lives < 2 or lives > 3:
                    board[i][j] = 0
                if lives == 3:
                    board[i][j] = 1
                
        # print(board)
        
        
        
        