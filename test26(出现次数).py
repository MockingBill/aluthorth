n = int(input())
a = [int(i) for i in input().split()]
res1 = 0
res5 = 0
res10 = 0
for i in a:
    if i == 1:
        res1 += 1
    elif i == 5:
        res5 += 1
    elif i == 10:
        res10 += 1
    else:
        pass
print(res1)
print(res5)
print(res10)
