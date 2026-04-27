class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(6)
res = [root.data]
def isLeaf(node):
    return node and not node.left and not node.right
def boundary_left(root):
    cur =  root.left
    while cur:
        if(not isLeaf(cur)):
            res.append(cur.data)
        if(cur.left):
            cur = cur.left
        else: 
            cur = cur.right
def boundary_leaf(root):
    if isLeaf(root):
        res.append(root.data)
    if root.left:
        boundary_leaf(root.left)
    if root.right:
        boundary_leaf(root.right)

def boundary_right(root):
    cur = root.right
    temp = []
    while(cur):
        if not isLeaf(cur):
            temp.append(cur.data)
        if cur.right:
            cur = cur.right
        else:
            cur = cur.left
    res.extend(temp[::-1])
boundary_left(root)
boundary_leaf(root)
boundary_right(root)
print(res)


