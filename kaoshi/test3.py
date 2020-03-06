n = int(input())
data = [int(d) for d in input().split()]
all = (n - 2) * 180
for k in data:
    all = all - k
print(all)
