class Solution:
    def __init__(self):
        self.sum = 0

    def go(self, i, j, m, n):
        if i == (m - 1) and j == (n - 1):
            self.sum = self.sum + 1
            return
        if i < m and j + 1 < n:
            self.go(i, j + 1, m, n)
        if i + 1 < m and j < n:
            self.go(i + 1, j, m, n)

    def uniquePaths(self, m, n):
        self.go(0, 0, m, n)
        return self.sum


a = Solution()
print(a.uniquePaths(1,3))

# 排列组合
# import math
# def uniquePaths(self, m: int, n: int) -> int:
#     return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))




