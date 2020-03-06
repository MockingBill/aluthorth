def isZero(a):
    if abs(a - 24) < 1e-8:
        return True


def GG(a, n):
    if n == 1:
        if isZero(a[0]):
            return True
        else:
            return False
    b = [float() for q in range(len(a) + 5)]
    for i in range(n-1):
        for j in range(i + 1, n):
            m = 0
            for k in range(n):
                if k != i and k != j:
                    b[m] = a[k]
                    m = m + 1
            b[m] = a[i] + a[j]
            if GG(b, m + 1):
                return True
            b[m] = a[i] - a[j]
            if GG(b, m + 1):
                return True
            b[m] = a[j] - a[i]
            if GG(b, m + 1):
                return True
            b[m] = a[i] * a[j]
            if GG(b, m + 1):
                return True
            if a[j] != 0:
                b[m] = a[i] / a[j]
                if GG(b, m + 1):
                    return True
            if a[i] != 0:
                b[m] = a[j] / a[i]
                if GG(b, m + 1):
                    return True
    return False


print(GG([5, 5, 5, 1], 4))
# data=[]
# while True:
#     row = [int(i.strip()) for i in input().split() if i.strip()]
#     if len([i for i in row if i != 0]) == 0:
#         break
#     else:
#         data.append(row)
# for row in data:
#     if GG(row, 4):
#         print("YES")
#     else:
#         print("NO")
