a=[[30,25,0],
[24,8,0],
[45,17,0],
[38,20,0],
[27,8,0],
[18,5,0],
[10,20,0]]
T=50
for i in range(len(a)):
    a[i][2]=a[i][0]-a[i][1]
a=sorted(a,key=lambda x:x[2])
sum=0
while len([i[1] for i in a if T>i[1]])!=0:
    for row in a:
        if row[1] <= T:
            sum = sum + row[0]
            T = T - row[1]
print(sum)
