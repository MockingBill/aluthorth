data = [int(d) for d in input().split()]
N = data[0]
K = data[1]
F=200
isbuy = False
for i in range(1, 21):
    if i==1:
        pass
    else:
        F = (K / 100) * F + F
    s = N * i

    if s >= F:
        isbuy = True
        print(i)
        break
if not isbuy:
    print('Impossible')
