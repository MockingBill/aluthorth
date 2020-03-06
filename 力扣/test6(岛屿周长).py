class Solution:
    def __init__(self):
        self.times = 0
        self.nums=0
        self.visited = None
        self.m = -1
        self.n = -1
        self.a = None

    def go(self, i, j):
        self.visited[i][j] = 1
        self.nums = self.nums + 1
        if self.isok(i + 1, j) and self.visited[i + 1][j] == 0 and self.a[i + 1][j] == 1:

            self.go(i + 1, j)
        if self.isok(i, j + 1) and self.visited[i][j + 1] == 0 and self.a[i][j + 1] == 1:

            self.go(i, j + 1)
        if self.isok(i - 1, j) and self.visited[i - 1][j] == 0 and self.a[i - 1][j] == 1:

            self.go(i - 1, j)
        if self.isok(i, j - 1) and self.visited[i][j - 1] == 0 and self.a[i][j - 1] == 1:

            self.go(i, j - 1)

    def isok(self, i, j):

        return 0 <= i < self.m and 0 <= j < self.n

    def numIslands(self, grid):

        if type(grid) == list and len(grid) > 0 and type(grid[0]) == list:
            self.a = grid
            self.m = len(grid)
            self.n = len(grid[0])
            self.visited = [[0 for j in range(self.n)] for i in range(self.m)]
            if self.m and self.n:
                for i in range(self.m):
                    for j in range(self.n):
                        if self.visited[i][j] == 0 and grid[i][j] == 1:
                            self.go(i, j)
                            self.times = self.times + 1
                # return self.times
                return self.nums
            else:
                return 0
        else:
            return 0


c = [[1,1],[1,1]]
s = Solution()
print(s.numIslands(c))
