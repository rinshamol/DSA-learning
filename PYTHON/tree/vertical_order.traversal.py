# using level order
from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(7)
root.right.right.left = TreeNode(6)


def vertical_order(root):
    if not root:
        return []
    res = []
    nodes = []
    que = deque([(root,0,0)])
    while que:
        node,x,y = que.popleft()
        nodes.append((x,y,node.data))
        if node.left:
            que.append((node.left,x-1,y+1))
        if node.right:
            que.append((node.right,x+1,y+1))
    nodes.sort()
    for x,y,val in nodes:
        res.append(val)
    print(res)
vertical_order(root)
# using inorder
def vo_inorder(root):
    if not root:
        return []
    res = []
    nodes = []
    x=y=0
    stack = []
    node = root
    while True:
        if node:
            stack.append((x,y,node))
            node = node.left
            if node:
                x -= 1
                y += 1
        else:
            if not stack:
                break
            a,b,val = stack.pop()
            nodes.append((a,b,val.data))
            node = val.right
            if node:
                x = a + 1
                y = b + 1
    nodes.sort()
    for x,y,val in nodes :
        res.append(val)        
    print(res)
vo_inorder(root)