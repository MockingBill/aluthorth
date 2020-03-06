T, M = 4, 3
a = [[10, 9],
     [2, 8],
     [9, 5],
     [8, 2]]
getMoney=max(sum([i[0] for i in a]),sum([i[1] for i in a]))
def do(i,j):
     
     k=-1
     if j==0:
          k=1
     else:
          k=0
     if i==(T-1):
          return a[i][j]



