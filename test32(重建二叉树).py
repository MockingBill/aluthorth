class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reTree(pre, tin):
    if len(pre) > 0:
        root = TreeNode(pre[0])
        rootid = tin.index(root.val)
        root.left = reTree(pre[1:1 + rootid], tin[:rootid])
        root.right = reTree(pre[1 + rootid:], tin[rootid + 1:])
        return root


def after_list(root):
    if root == None:
        return
    after_list(root.left)
    after_list(root.right)
    print(root.val, end="")



data=[]
try:
    while True:

        a=input().split()
        data.append(tuple(a))

except Exception as err:
    pass

for pre,mid in data:

    root=reTree(pre,mid)
    after_list(root)
    print()
