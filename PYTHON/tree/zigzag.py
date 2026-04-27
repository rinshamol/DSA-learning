from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
def zig_zag(node):
    if not node:
        return []
    que = deque([node])
    isltof = True
    result = []
    while que:
        size = len(que)
        row = [0]*size
        for i in range(0,size):
            node = que.popleft()
            index = i if isltof else (size-1-i)
            row[index] = node.data
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        result.extend(row)
        isltof = not isltof
    print(result)
zig_zag(root)