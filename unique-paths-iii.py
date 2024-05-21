class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != -1: count += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return Solution.bfs(self, grid, i, j, [], count)
    
    def bfs(self, grid, i, j, searched, count):
        if grid[i][j] == 2:
            if count == len(searched) + 1:
                return 1
            return 0
        
        m = len(grid)
        n = len(grid[0])
        s = 0

        searchedNew = searched.copy()
        searchedNew.append((i, j))

        if i < m - 1 and grid[i + 1][j] != -1 and (i + 1, j) not in searched:
            s += Solution.bfs(self, grid, i + 1, j, searchedNew, count)
        
        if j < n - 1 and grid[i][j + 1] != -1 and (i, j + 1) not in searched:
            s += Solution.bfs(self, grid, i, j + 1, searchedNew, count)
        
        if i > 0 and grid[i - 1][j] != -1 and (i - 1, j) not in searched:
            s += Solution.bfs(self, grid, i - 1, j, searchedNew, count)

        if j > 0 and grid[i][j - 1] != -1 and (i, j - 1) not in searched:
            s += Solution.bfs(self, grid, i, j - 1, searchedNew, count)

        return s