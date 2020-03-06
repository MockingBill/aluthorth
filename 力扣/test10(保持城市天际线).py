class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        sum=0
        b = [[0 for j in row] for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                row_max = max(grid[i])
                col_max = max([grid[q][j] for q in range(len(grid))])
                Incremental=min(row_max, col_max)-grid[i][j]
                if Incremental>0:
                    sum+=Incremental

        return sum


