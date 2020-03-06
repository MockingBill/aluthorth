def HowMuch(i, j):
    global room_block
    if visted[i][j] != 0:
        return
    room_block = room_block + 1
    visted[i][j] = 1
    # 西左
    if wall[i][j] & 1 == 0 and visted[i][j - 1] == 0:
        HowMuch(i, j - 1)
    # 北上
    if wall[i][j] & 2 == 0 and visted[i - 1][j] == 0:
        HowMuch(i - 1, j)
    # 东右
    if wall[i][j] & 4 == 0 and visted[i][j + 1] == 0:
        HowMuch(i, j + 1)
    # 南下
    if wall[i][j] & 8 == 0 and visted[i + 1][j] == 0:
        HowMuch(i + 1, j)


RC = list(map(int, input().split()))
if len(RC) == 1:
    row_num = RC[0]
    col_num = int(input())
else:
    row_num, col_num = RC
wall=[]
for i in range(row_num):
    wall.append(list(map(int,input().split())))

visted = [[0 for j in range(col_num)] for i in range(row_num)]
max_room_block = 0
rooms_nums = 0
for h in range(row_num):
    for o in range(col_num):
        if visted[h][o] == 0:
            room_block = 0
            rooms_nums = rooms_nums + 1
            HowMuch(h, o)
            max_room_block = max(max_room_block, room_block)
print(rooms_nums)
print(max_room_block)
