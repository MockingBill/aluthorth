maxRoomArea=roomNum=roomArea=0
def Dfs(i,k):
    global roomNum,roomArea
    if color[i][k]:
        return
    roomArea=roomArea+1
    color[i][k]=roomNum
    # 西左
    if rooms[i][k] & 1 == 0 and color[i][k - 1] == 0:
        Dfs(i, k - 1)
    # 北上
    if rooms[i][k] & 2 == 0 and color[i - 1][k] == 0:
        Dfs(i - 1, k)
    # 东右
    if rooms[i][k] & 4 == 0 and color[i][k + 1] == 0:
        Dfs(i, k + 1)
    # 南下
    if rooms[i][k] & 8 == 0 and color[i + 1][k] == 0:
        Dfs(i + 1, k)
RC=list(map(int,input().split()))
if len(RC)==1:
    R=RC[0]
    C=int(input())
else:
    R,C=RC
rooms=[[]]
color=[[0 for i in range(C+2)] for i in range(R+2)]
for i in range(R):
    rooms.append([0]+list(map(int,input().split())))
for i in range(1,R+1):
    for k in range(1,C+1):
        if not color[i][k]:
            roomNum+=1
            roomArea=0
            Dfs(i,k)
            maxRoomArea=max(roomArea,maxRoomArea)
print(roomNum)
print(maxRoomArea)
