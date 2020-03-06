def getTimes(a):
    a = sorted(a, key=lambda x: x[1])
    cu_last = a[0]
    times = 1
    step = 0
    for g in range(len(a)):
        for i in range(step, len(a)):
            if a[i][0] >= cu_last[1]:
                cu_last = a[i]
                times = times + 1
                step = i
                break
    print(times)

ArrayData=[]
while True:
    n=int(input().strip())
    if n==0:
        break
    singleArray=[]
    for i in range(n):
        singleArray.append([int(q.strip()) for q in input().split() if q.strip()!=""])
    ArrayData.append(singleArray)
for data in ArrayData:
    getTimes(data)
