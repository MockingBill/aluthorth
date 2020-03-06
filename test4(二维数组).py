def waiwei(data, row_n, col_n):
    if row_n == 1:
        for i in data[0]:
            print(i)
    elif col_n == 1:
        for i in data:
            print(i[0])
    elif row_num != 1 and col_num != 1:
        step = [0, 0]
        times = col_n + (row_n - 1) + (col_n - 1) + row_n - 2
        if times == 0:
            times = 1
        for s in range(times):
            print(data[step[0]][step[1]])
            pos = (step[0], step[1])
            if pos in has_array:
                data[pos[0]][pos[1]] = "@"
                has_array.remove(pos)
            if step[0] == 0 and step[1] < (col_n - 1):
                step[1] = step[1] + 1
            elif step[0] < (row_n - 1) and step[1] == col_n - 1:
                step[0] = step[0] + 1
            elif step[0] == row_n - 1 and step[1] <= (col_n - 1) and step[1] > 0:
                step[1] = step[1] - 1
            elif step[0] <= row_n - 1 and step[0] > 0 and step[1] == 0:
                step[0] = step[0] - 1


def train(arr):
    resu = []
    for row in arr:
        eff = []
        for j in row:
            if j != "@":
                eff.append(j)
        if len(eff) != 0:
            resu.append(eff)
    return resu


def main_y(data, row_num, col_num):
    while row_num > 0 and col_num > 0:
        waiwei(data, row_num, col_num)
        data = train(data)
        row_num = row_num - 2
        col_num = col_num - 2
has_array = []
row_col_num = input().split()
row_col_num = [int(q) for q in row_col_num if q.strip()]
data = []
for times in range(row_col_num[0]):
    row = input()
    row_v = [int(q) for q in row.split() if q.strip()]
    data.append(row_v)

row_num = row_col_num[0]
col_num = row_col_num[1]
for i in range(row_num):
    for j in range(col_num):
        has_array.append((i, j))

main_y(data, row_num, col_num)




