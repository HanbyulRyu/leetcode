class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(len(grid)) :
            for j in range(len(grid[i])):
                if i == 0 or j == 0:
                    grid[i][j] = 1
       
        # [1, 1, 1, 1, 1, 1, 1]
        # [1, 0, 0, 0, 0, 0, 0]
        # [1, 0, 0, 0, 0, 0, 0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        # [1, 1, 1, 1, 1, 1, 1]
        # [1, 2, 3, 4, 5, 6, 7]
        # [1, 3, 6, 10, 15, 21, 28]
  
        return grid[m-1][n-1]
        
#         global result
#         result = 0
        
#         def paint(i, j):
#             global result
#             if i == m-1 or j == n-1:
#                 result += 1
#                 return
                
#             if i < m-1:
#                 paint(i+1, j)

#             if j < n-1:
#                 paint(i, j+1)
            
#         paint(0, 0)
        
#         return result
                
            
        