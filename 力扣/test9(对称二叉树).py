class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def giveValue(node, val):
    if val <= 0:
        return
    node.val = next(cc)
    node.left = TreeNode(next(cc))
    node.right = TreeNode(next(cc))
    giveValue(node.left, val - 1)
    giveValue(node.right, val - 1)


# 先序 根左右
def pre(root):
    if root == None:
        return
    print(root.val, end=" ")
    pre(root.left)
    pre(root.right)


# 中序 左根右
def mid(root):
    if root == None:
        return
    mid(root.left)
    print(root.val, end=" ")
    mid(root.right)


# 中序 左根右
def back(root):
    if root == None:
        return
    back(root.left)
    back(root.right)
    print(root.val, end=" ")


def genw():
    n = 65
    while True:
        yield chr(n)
        n = n + 1


cc = genw()
t = TreeNode(0)
giveValue(t, 2)


r=TreeNode(0)
r.left=TreeNode(1)
r.right=TreeNode(0)
r.left.left=TreeNode(0)
r.left.right=TreeNode(0)
r.right.left=TreeNode(0)
r.right.right=TreeNode(0)
"".replace()

def isSymmetric(root):
    return isMirror(root.left, root.right)


def isMirror(t1, t2):
    if t1 == None and t2 == None: return True
    if t1 == None or t2 == None: return False
    return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
print(1 and 1)



