from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y:(x+1,y),#下
    lambda x,y:(x,y-1),#左
    lambda x,y:(x,y+1),#右
    lambda x,y:(x-1,y),#上
]

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2]) # 把起点放进去
    realpath.reverse()
    print(len(realpath))
    for i in realpath:
        print(i)

def maze_path_queue(x1,y1,x2,y2):
    maze[x1][y1]=2
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue)>0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                # 后续节点进队，记录哪个节点带他来的
                node = (nextNode[0],nextNode[1],len(path)-1)
                queue.append(node)
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已经走过
    else:
        print('没有路')
        return False
maze_path_queue(1,1,8,8)