data = [int(d) for d in input().split()]
m = data[0]
n = data[1]
sum = 0
for i in range(m, n + 1):
    if i % 17 == 0:
        sum = sum + i
print(sum)
