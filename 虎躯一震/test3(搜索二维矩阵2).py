a = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]

'''从右上角开始，大了往左走，小了往下走'''
'''从左下角开始，大了往上走，小了往右走'''

class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] > target:
                j = j - 1
            elif matrix[i][j] < target:
                i = i + 1
            else:
                return True
        return False


s = Solution()
for k in [(i,j) for j in range(5) for i in range(5)]:
    print(s.searchMatrix(a, a[k[0]][1]))
