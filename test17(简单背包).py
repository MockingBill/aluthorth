def judge(w,k):
    if w == 0:
        return 1
    if k <=0:
        return 0
    return judge(w,k-1)+judge(w-a[k-1],k-1)

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
print(judge(40,n))
