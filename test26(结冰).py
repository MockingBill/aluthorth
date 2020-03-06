data = []
while True:
    fist = input()
    if fist == "0 0":
        break
    else:
        n = int(fist.split(" ")[0])
        m = int(fist.split(" ")[1])
        wall = []
        for r in range(n):
            text = input()
            wall.append([i for i in text])
        data.append([n, m, wall])
for item in data:
    n = item[0]
    m = item[1]
    wall = item[2]
    visted = [[0 for j in range(m)] for i in range(n)]


    def isOkIJ(i, j):
        global n, m
        if 0 <= i < n and 0 <= j < m:
            return True
        else:
            return False


    def go(i, j):
        if visted[i][j] != 0:
            return
        visted[i][j] = 1
        # 西左
        if isOkIJ(i, j - 1) and wall[i][j - 1] == '@':
            go(i, j - 1)
        # 北上
        if isOkIJ(i - 1, j) and wall[i - 1][j] == '@':
            go(i - 1, j)
        # 东右
        if isOkIJ(i, j + 1) and wall[i][j + 1] == '@':
            go(i, j + 1)
        # 南下
        if isOkIJ(i + 1, j) and wall[i + 1][j] == '@':
            go(i + 1, j)
        if isOkIJ(i + 1, j + 1) and wall[i + 1][j + 1] == '@':
            go(i + 1, j + 1)
        if isOkIJ(i - 1, j - 1) and wall[i - 1][j - 1] == '@':
            go(i - 1, j - 1)
        if isOkIJ(i - 1, j + 1) and wall[i - 1][j + 1] == '@':
            go(i - 1, j + 1)
        if isOkIJ(i + 1, j - 1) and wall[i + 1][j - 1] == '@':
            go(i + 1, j - 1)


    ice_num = 0
    for h in range(n):
        for o in range(m):
            if visted[h][o] == 0 and wall[h][o] == "@":
                ice_num = ice_num + 1
                go(h, o)
    print(ice_num)

