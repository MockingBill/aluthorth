p_n = int(input())
data = []
for i in range(p_n):
    text = input()
    z = [i for i in text.split(" ") if i.strip() != ""]
    z[1] = int(z[1])
    data.append(z)
old = [i for i in data if i[1] >= 60]
young = [i for i in data if i[1] < 60]


def s_v(a):
    return a[1]


old = sorted(old, key=s_v,reverse=True)
for i in old:
    print(i[0])
for i in young:
    print(i[0])
