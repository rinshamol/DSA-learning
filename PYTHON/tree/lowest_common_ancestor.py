class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.left = TreeNode(4)

def lca(node, p, q):
    if not node or node.data == p or node.data == q:
        return node
    l = lca(node.left, p, q)
    r = lca(node.right, p, q)
    if not l :
        return r
    elif not r:
        return l
    else:
        return node
res = lca(root,4,7)
print(res.data)