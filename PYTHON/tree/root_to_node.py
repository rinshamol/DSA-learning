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
ds = []
def node_to_root(node, x,ds):
    if not node:
        return False
    ds.append(node.data)
    
    if node.data == x :
        return True
    if node_to_root(node.left,x,ds) or node_to_root(node.right,x,ds):
        return True
    ds.pop()
    return False
if node_to_root(root,7,ds):
    print(ds)