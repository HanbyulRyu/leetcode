class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_r = len(board)
        max_c = len(board[0])

        def dfs(r, c, word):
            if not word:
                return True

            # add1 : 이미 지나온 곳 표기
            temp = board[r][c]
            board[r][c] = "0"
            
            if 0 <= r+1 < max_r and 0 <= c < max_c and board[r+1][c] == word[0]:
                if dfs(r+1, c, word[1:]):
                    return True
                
            if 0 <= r-1 < max_r and 0 <= c < max_c and board[r-1][c] == word[0]:
                if dfs(r-1, c, word[1:]):
                    return True
                
            if 0 <= r < max_r and 0 <= c+1 < max_c and board[r][c+1] == word[0]:
                if dfs(r, c+1, word[1:]):
                    return True
                
            if 0 <= r < max_r and 0 <= c-1 < max_c and board[r][c-1] == word[0]:
                if dfs(r, c-1, word[1:]):
                    return True

            # add2 : 이미 지나온 곳이지만 다시 처음부터 시작할 수도 있음 (롤백)
            board[r][c] = temp
                
        for i in range(max_r):
            for j in range(max_c):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:]):
                        return True

        return False