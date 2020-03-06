class node:
    def __init__(self, x, y, h):  # 存储树的坐标和高度
        self.x = x
        self.y = y
        self.h = h


    def __lt__(self, other):  # 重载小于号
        return self.h < other.h


class Solution:
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self):
        self.grade = 1

    def minStep(self, forest, start, tree, m, n):  # bfs
        step = 0
        visited = [[0 for i in range(0, n)] for i in range(0, m)]
        q = []
        q.append(start)
        visited[start.x][start.y] = 1

        while len(q):
            size = len(q)
            for i in range(0, size):  # 确保循环内搜索的点与搜索起点的距离相同
                curr = q[0]
                del q[0]
                if curr.x == tree.x and curr.y == tree.y:
                    return step
                for j in range(0, 4):
                    nr = curr.x + self.dir[j][0]
                    nc = curr.y + self.dir[j][1]

                    if nr < 0 or nr >= m or nc < 0 or nc >= n or forest[nr][nc] == -1 or visited[nr][nc] == 1 or \
                            forest[nr][nc] > self.grade:
                        continue
                    q.append(node(nr, nc, forest[nr][nc]))
                    visited[nr][nc] = 1
            step += 1
        return -1

    def beat(self, forest):
        # write your code here
        if len(forest) == 0:
            return 0
        m = len(forest)
        n = len(forest[0])
        pq = []
        self.grade = 1
        for i in range(0, m):
            for j in range(0, n):
                if forest[i][j] == -99:
                    target_x = i
                    target_y = j
                    forest[i][j] = 0
                if forest[i][j] > 0:
                    pq.append(node(i, j, forest[i][j]))  # 存入妖精的坐标和等级
        pq.sort()  # 按照等级排序

        start = node(0, 0, forest[0][0])  # 小黑的等级和位置
        sum_step = 0  # 总共需要的步数
        if len(pq) == 0:  # 没有妖怪
            return target_x + target_y
        while len(pq):
            tree = pq[0]
            del pq[0]
            #
            step = self.minStep(forest, start, tree, m, n)
            self.grade = self.grade + 1
            if step < 0:
                return -1
            sum_step += step

            start.x = tree.x  # 将当前树的坐标设为下一次搜索的起点
            start.y = tree.y
            start.h = tree.h

        sum_step = sum_step + abs(target_x - tree.x) + abs(target_y - tree.y)
        return sum_step



