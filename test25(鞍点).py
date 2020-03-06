def isAn(i, j):
    if i == 0 and j == 4:
        pass
    max_row = max(a[i])
    s = len([1 for f in a[i] if max_row > f])
    if s != 4:
        return False
    else:
        if max_row == a[i][j]:
            col = []
            for k in range(5):
                col.append(a[k][j])
            col_min = min(col)
            d = len([1 for n in col if col_min < n])
            if d != 4:
                return False
            if min(col) == a[i][j]:
                return True
            else:
                return False
        else:
            return False


a = []
b = []
for q in range(5):
    r = [int(l) for l in input().split()]
    if len(r) == 25:
        b = r
        break
    elif len(r) == 5:
        a.append(r)
    else:
        pass
if len(b) != 0:
    for i in [0, 5, 10, 15, 20]:
        a.append(b[0 + i:5 + i])
resu = []

for i in range(5):
    for j in range(5):
        if isAn(i, j):
            resu.append((i + 1, j + 1, a[i][j]))
            break

if len(resu) != 0:
    for row in resu:
        print(row[0], row[1], row[2])
else:
    print("not found")
