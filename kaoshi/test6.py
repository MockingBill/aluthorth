def getCouple(m, data):
    res = []
    for i in range(len(data)):
        for j in range(i):
            if data[j] * data[i] == m or data[j] + data[i] == m:
                zzz = (data[i], data[j])
                res.append((min(zzz), max(zzz)))
    if len(res) == 0:
        return 'NONE'
    res = list(set(res))

    res = sorted(res, key=lambda x: x[0])
    for i in range(len(res)):
        for j in range(i):
            if res[i][0] == res[j][0]:
                if res[i][1] % 3 == 0 and res[j][1] % 3 != 0:
                    res[i], res[j] = res[j], res[i]
                elif res[i][1] % 3 == 0 and res[j][1] % 3 == 0:
                    if res[i][1] > res[j][1]:
                        res[i], res[j] = res[j], res[i]
                elif res[i][1] % 3 != 0 and res[j][1] % 3 != 0:
                    if res[i][1] < res[j][1]:
                        res[i], res[j] = res[j], res[i]
    test = ""

    for pos, kbj in enumerate(res):

        if pos == (len(res) - 1):
            test = test + "(" + str(kbj[0]) + "," + str(kbj[1]) + ")"
        else:
            test = test + "(" + str(kbj[0]) + "," + str(kbj[1]) + "),"
    return test


ar_n = int(input())
m_arr = []
data_arr = []
for kkkk in range(ar_n):
    m_arr.append(int(input()))
    data_arr.append([int(qj) for qj in input().split()])
for jbk in range(ar_n):
    text = getCouple(m_arr[jbk], data_arr[jbk])
    if jbk == (ar_n - 1):
        print(text, end="")
    else:
        print(text)
