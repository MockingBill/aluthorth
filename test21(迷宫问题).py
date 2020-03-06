class dque(object):
    def __init__(self):
        self.deque = []
        self.head = 0
        self.tail = 0

    def put(self, item):
        self.deque.append(item)
        self.tail += 1

    def get(self):
        a = self.deque[self.head]
        self.head += 1
        return a

    def isemort(self):
        if self.head == self.tail:
            return True
        else:
            return False


class point(object):
    def __init__(self, i, j, pre):
        self.i = i
        self.j = j
        self.pre = pre


def isOkIJ(i, j):
    global row, col
    if 0 <= i < 5 and 0 <= j < 5 and maze[i][j] != 1:
        return True
    else:
        return False


def return_start(p):
    result.append("(" + str(p.i) + ", " + str(p.j) + ")")
    if p.pre == None:
        return
    else:
        return return_start(p.pre)


maze = []
for i in range(5):
    maze.append([int(text.strip()) for text in input().split() if text.strip() != ""])
result = []
que = dque()
que.put(point(0, 0, None))

while not que.isemort():
    p = que.get()
    i = p.i
    j = p.j
    if i == 4 and j == 4:
        return_start(p)
        break
    if isOkIJ(i + 1, j):
        que.put(point(i + 1, j, p))
    if isOkIJ(i, j + 1):
        que.put(point(i, j + 1, p))
    if isOkIJ(i - 1, j):
        que.put(point(i - 1, j, p))
    if isOkIJ(i, j - 1):
        que.put(point(i, j - 1, p))
for i in result[-1::-1]:
    print(i)
