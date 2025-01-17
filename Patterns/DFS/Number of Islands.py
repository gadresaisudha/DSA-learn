class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = 0
        def dfs(r,c):
            
            if r<0 or c<0 or r>=rows or c>=columns or grid[r][c]=="0":
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        


        for i in range(rows):
            for j in range(columns):
                if grid[i][j]== "1":
                    dfs(i,j)
                    res+=1

        
        return res