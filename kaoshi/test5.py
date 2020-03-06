n, m, k = tuple([int(i) for i in input().split()])
a = []
b = []
for uu in range(n):
    a.append([int(hh) for hh in input().split()])
for jj in range(m):
    b.append([int(hh) for hh in input().split()])


def getRow(r_n, A):
    return A[r_n]


def getCol(c_n, A):
    col = []
    for i in range(len(A)):
        col.append(A[i][c_n])
    return col


def doMut(a, b):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i] * b[i]
    return sum


res = [['' for j in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        res[i][j] = doMut(getRow(i, a), getCol(j, b))

for ee in res:
    for qq in ee:
        print(qq,end=" ")
    print()
