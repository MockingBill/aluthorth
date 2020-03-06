def do(data):
    words = []
    res_words = {}
    for d in data:
        words.extend(d.keys())
    for w in words:
        for di_ge in data:

            if w in di_ge and w not in res_words:
                res_words[w] = [di_ge[w]]
            elif w in di_ge and w in res_words:
                res_words[w].append(di_ge[w])
    for k,v in res_words.items():
        if len(v)==1:
            res_words[k]=v[0]
        elif len(v)>1:
            res_words[k]=(sum(v)/len(v))


    s_res=sorted(list(res_words.items()), key=lambda x: x[1])
    return s_res[0][0]


n = int(input())
arrData = []
for arr in range(n):
    N = int(input())
    data = []
    for i in range(N):
        d = {}
        for qq in range(10):
            ddd = input().split()
            d[ddd[0]] = int(ddd[1])
        data.append(d)
    arrData.append(data)
for pos,d23 in enumerate(arrData):
    res_text=do(d23)
    if pos==(len(arrData)-1):
        print(res_text,end="")
    else:
        print(res_text)

