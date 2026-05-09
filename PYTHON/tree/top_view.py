from collections import deque, defaultdict
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)



# Top View
def top_view(root):
    if not root:
        return []
    min_x = max_x = 0
    res = defaultdict(int)
    que = deque([(0,root)])
    while que:
        x,node = que.popleft()
        if not x in res:
            res[x] = node.data
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        if node.left:
            que.append((x-1,node.left))
        if node.right:
            que.append((x+1, node.right))
    result = []
    for i in range(min_x, max_x + 1):
        result.append(res[i])
    print(result)
top_view(root)
# bottom view
def bottom_view(root):
    if not root:
        return []
    min_x = max_x = 0
    res = defaultdict(int)
    que = deque([(0,root)])
    while que:
        x,node = que.popleft()
        res[x] = node.data
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        if node.left:
            que.append((x-1,node.left))
        if node.right:
            que.append((x+1, node.right))
    result = []
    for i in range(min_x, max_x + 1):
        result.append(res[i])
    print(result)
bottom_view(root)
root.left.right.left = TreeNode(8)
# Right View
def right_view(node,level,ds):
    if not node:
        return
    if level == len(ds):
        ds.append(node.data)
    right_view(node.right,level+1,ds)
    right_view(node.left,level+1,ds)
ds = []
right_view(root,0,ds)
print(ds)
# Left View
def left_view(node,level,ds):
    if not node:
        return
    if level == len(ds):
        ds.append(node.data)
    left_view(node.left,level+1,ds)
    left_view(node.right,level+1,ds)
    
dp = []
left_view(root,0,dp)
print(dp)