def outputArray(row, col, a):
    if row == 1:
        i, j = 0, 0
        for k in range(1, col):
            print(a[i][j])
            j = j + 1

    elif col == 1:
        i, j = 0, 0
        for k in range(1, col):
            print(a[i][j])
            i = i + 1

    else:
        i, j = 0, 0
        count = row * col
        while (count > 0):
            if i > 100:
                break
            for k in range(1, col):
                count = count - 1
                print(a[i][j])
                j = j + 1

            for k in range(1, row):
                count = count - 1
                print(a[i][j])
                i = i + 1

            for k in range(1, col):
                count = count - 1
                print(a[i][j])
                j = j - 1

            for k in range(1, row):
                count = count - 1
                print(a[i][j])
                i = i - 1

            i = i + 1
            j = j + 1
            row = row - 2
            col = col - 2
            if row == 1:
                for k in range(0, col):
                    count = count - 1
                    print(a[i][j])
                    j = j + 1

            elif col == 1:
                for k in range(0, row):
                    count = count - 1
                    print(a[i][j])
                    i = i + 1


row_col_num = [int(q) for q in input().split() if q.strip()]
data = []
for times in range(row_col_num[0]):
    row = input()
    row_v = [int(q) for q in row.split() if q.strip()]
    data.append(row_v)
outputArray(row_col_num[0], row_col_num[1], data)
