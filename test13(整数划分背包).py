# 生成器解
# def sp(n, m):
#     if n < m:
#         raise StopIteration
#     else:
#         for i in range(m, n // 2 + 1):
#             for l in sp(n - i, i):
#                 yield [i] + l
#         yield [n]
# def getNum(num):
#     resu = []
#     for i in sp(num, 1):
#         resu.append(i)
#     print(len(resu))
#
# numarray = []
# try:
#     while True:
#         numarray.append(int(input()))
# except Exception:
#     pass
# [getNum(i) for i in numarray]

# 递归解
def getNum(n,m):
    if n==1 or m==1:
        return 1
    elif m==n:
        return 1+getNum(n,m-1)
    elif m>n:
        return getNum(n,n)
    else:
        return getNum(n, m - 1) + getNum(n - m, m)
numarray = []
try:
    while True:
        numarray.append(int(input()))
except Exception:
    pass
for i in numarray:
    print(getNum(i,i))
