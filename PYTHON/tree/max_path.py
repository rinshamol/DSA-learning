class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(10)
root.left = TreeNode(-20)
root.left.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)
maxi = [0]
def max_path(node,maxi):
    if not node:
        return 0
    l = max(0,max_path(node.left,maxi))
    r = max(0,max_path(node.right,maxi))
    maxi[0] = max(maxi[0],l+r+node.data)
    return node.data + max(l,r)
max_path(root,maxi)
print(maxi[0])