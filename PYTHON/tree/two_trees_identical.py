class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.left = TreeNode(4)
p.right.right = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.right.left = TreeNode(4)
# q.right.right = TreeNode(5)

def is_identical(p,q):
    if not p or not q :
        return p == q
    return (p.data == q.data) and is_identical(p.left,q.left) and is_identical(p.right,q.right)
print(is_identical(p,q))