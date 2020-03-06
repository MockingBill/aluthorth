g_num = int(input())
data = []
for i in range(g_num):
    n = int(input())
    row = []
    for k in range(n):
        row.append(int(input()))
    data.append(row)
for a in data:
    a = sorted(a)
    if len(a) % 2 == 0:
        l1 = len(a) / 2
        l2 = len(a) / 2 - 1

        res = (a[int(l1)] + a[int(l2)]) / 2
        print("%.1f" % res)
    elif len(a) % 2 == 1:
        l = (len(a) - 1) / 2
        print(a[int(l)])
