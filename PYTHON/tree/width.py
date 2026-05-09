from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.right = TreeNode(50)
root.left.left = TreeNode(60)
root.right.right = TreeNode(40)

def width(node,ind):
    if not node:
        return 0
    res = 0
    que = deque([(node,ind)])
    while que:
        size = len(que)
        mini = que[0][1]
        first = last = 0
        for i in range(0,size ):
            n, x = que.popleft()
            cur_i = x - mini
            if i == 0:
                first = cur_i
            if i == size - 1:
                last = cur_i
            if n.left :
                que.append((n.left, 2*cur_i + 1))
            if n.right:
                que.append((n.right,2*cur_i + 2))
        res = max(res, (last - first) + 1)
    print(res)
width(root,0)