visted = [[0 for j in range(50)] for i in range(50)]


def way(i, j, n):
    # 没有步数就是不动，只有0种走法
    if n == 0:
        return 1
    else:
        # 来了就先改变占位
        visted[i][j] = 1
        num = 0
        if visted[i + 1][j] == 0:
            num += way(i + 1, j, n - 1)
        if visted[i][j + 1] == 0:
            num += way(i, j + 1, n - 1)
        if visted[i][j - 1] == 0:
            num += way(i, j - 1, n - 1)
        visted[i][j] = 0
        return num


n = int(input())
print(way(0, 25, n))
