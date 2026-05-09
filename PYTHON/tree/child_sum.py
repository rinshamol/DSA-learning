from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
p = TreeNode(50)
p.left = TreeNode(7)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(5)
p.right.left = TreeNode(1)
p.right.right = TreeNode(30)
def child_sum(root):
    if not root:
        return
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    if child >= root.data:
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data
    child_sum(root.left)
    child_sum(root.right)
    tot = 0
    if root.left :
        tot += root.left.data
    if root.right:
        tot += root.right.data
    if root.left or root.right:
        root.data = tot
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
level_order(p)
print(" ")
child_sum(p)
level_order(p)
