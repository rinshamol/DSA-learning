class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(7)
root.right.left.left.left = TreeNode(8)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
d = [0]
def diameter(root,d):
    if not root:
        return 0
    l = diameter(root.left,d)
    r = diameter(root.right,d)
    d[0] = max(d[0],l+r)
    return 1 + max(l,r)
diameter(root,d)
print(d[0])
