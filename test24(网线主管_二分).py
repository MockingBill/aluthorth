text = [int(i) for i in input().split()]
a = []
for i in range(text[0]):
    a.append(float(input()))
n = text[0]
m = text[1]
s = 0


def find(x):
    h = 0
    for i in range(n):
        h = h + a[i] / x
    return h


for i in range(n):
    a[i] = (a[i] * 100 + 3)
    s += a[i]
l = 0
r = s / m
while (l <= r):
    mid = (l + r + 1) / 2
    c = 0
    for i in range(n):
        c += a[i] // mid
    if c >= m:
        l = mid
    else:
        r = mid - 1
print("%.2f" % ((l - 1) / 100.0))
