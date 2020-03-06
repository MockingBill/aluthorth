def putApple(m,n):
    if m==0 or n==1:
        return 1
    if(n>m):
        return putApple(m,m)
    else:
        return putApple(m,n-1)+putApple(m-n,n)


n=int(input())
data=[]
for i in range(n):
    data.append([int(row) for row in input().split()])
for row in data:
    print(putApple(row[0],row[1]))



