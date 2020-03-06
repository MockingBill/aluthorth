def getSection(x, y, d):
    dis = (d ** 2 - y ** 2) ** 0.5
    return [x - dis, x + dis]


def isCovered(a, b):
    if max(a[0], b[0]) <= min(a[1], b[1]):
        return True


def allisCoverd(lst):
    flag = True
    for k in range(len(lst)):
        for j in range(k, len(lst)):
            if k != j and not isCovered(lst[k], lst[j]):
                flag = False
    return flag


def getRadarNum(n, d, data):
    sectArray = []
    for item in data:
        sectArray.append(getSection(item[0], item[1], d))
    sordSec = sorted(sectArray, key=lambda qi: qi[0])

    stack = []
    sum = 0
    for p, v in enumerate(sordSec):
        stack.append(v)
        if allisCoverd(stack):
            pass
        else:
            sum = sum + 1
            stack.clear()
            stack.append(v)
    return sum + 1

# ArrayData = []
# while True:
#     text = input()
#     if text == "0 0":
#         break
#     else:
#         row = [int(i) for i in text.split()]
#     if len(row) != 0:
#         n = row[0]
#         d = row[1]
#         data = []
#         for i in range(n):
#             data.append([int(pos) for pos in input().split()])
#         ArrayData.append((n, d))
#         ArrayData.append(data)
#     else:
#         continue
# print(ArrayData)
ArrayData=[(4, 2), [[1, 2], [-3, 1], [2, 1],[8,2],[8,1]], (1, 2), [[0, 2]]]
xunhuan_times = 1
for k, group in enumerate(ArrayData):
    if type(group) == tuple:
        num = getRadarNum(group[0], group[1], ArrayData[k + 1])
        print("Case " + str(xunhuan_times) + ": " + str(num))
        xunhuan_times += 1
