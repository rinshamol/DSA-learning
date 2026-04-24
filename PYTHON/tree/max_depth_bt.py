from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(5)
root.right.right = TreeNode(7)

# recurssive
def max_depth_r(node):
    if not node:
        return 0
    l = max_depth_r(node.left)
    r = max_depth_r(node.right)
    return (1 + max(l,r))
# print(max_depth_r(root))
# level order
def max_depth_l(node):
    if not node:
        return
    que = deque([root])
    depth = 0
    while que:
        level_size = len(que)
        for _ in range(level_size):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        depth += 1
    print(depth)
max_depth_l(root)

