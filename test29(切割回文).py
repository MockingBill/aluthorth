def getSingleStr(a):
    a_ = a[-1::-1]
    flag = False
    for k in range(len(a_), 0, -1):
        for j in range(len(a_) - k, -1, -1):
            if a_[j:j + k] in a:
                if a_[j:j + k] in a:
                    return (a_[j:j + k])
try:
    n = int(input())
    data = []
    for i in range(n):
        data.append(input())
except:
    pass
for a in data:
    s = ""
    times = 0
    while True:
        if s == a or s == a[-1::-1] or len(a) == 0:
            break
        q = getSingleStr(a)
        s = s + q
        a = a.replace(q, "")
        times += 1
    print(times - 1)
