def isOkIJ(i, j):
    global row, col
    if 0 <= i < row and 0 <= j < col:
        return True
    else:
        return False
def go(i, j):
    global black_num
    if visted[i][j] or not isOkIJ(i, j):
        return
    visted[i][j] = 1
    black_num = black_num + 1

    if isOkIJ(i, j - 1) and wall[i][j - 1] == '.':
        go(i, j - 1)
    if isOkIJ(i - 1, j) and wall[i - 1][j] == '.':
        go(i - 1, j)
    if isOkIJ(i, j + 1) and wall[i][j + 1] == '.':
        go(i, j + 1)
    if isOkIJ(i + 1, j) and wall[i + 1][j] == '.':
        go(i + 1, j)
All_DATA=[]
while True:
    r1 = [int(item) for item in input().split() if item.strip() != ""]
    col, row = r1[0], r1[1]
    wall=[]
    if col==0 and row==0:
        break
    for item in range(row):
        text = input()
        wall.append([kk for kk in text])
    All_DATA.append([(col,row),wall])
for data in All_DATA:
    col,row=data[0][0],data[0][1]
    wall=data[1]
    s_i = 0
    s_j = 0
    stop = False
    for i in range(row):
        for j in range(col):
            if wall[i][j] == "@":
                s_i = i
                s_j = j
            if stop:
                break
        if stop:
            break

    black_num = 0
    visted = [[0 for j in range(col)] for i in range(row)]
    go(s_i, s_j)
    print(black_num)
