from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(root)

def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data)
    in_order(node.right)
def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data)
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
# pre_order_traversal(root)
# in_order(root)
# post_order(root)
# level_order(root)
# using stack
def pre_order_s(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data,end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# pre_order_s(root)

def in_order_s(root):
    if not root:
        return
    stack = []
    node = root
    while True:
        if node :
            stack.append(node)
            node = node.left
        else:
            if not stack:
                return
            node = stack.pop()
            print(node.data, end=" ")
            node = node.right
# in_order_s(root)

def post_order_s(node):
    if not node:
        return
    s1 = [node]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        a = s2.pop()
        print(a.data, end=" ")
# post_order_s(root)

# postorder using single stack
def post_order_s1(root):
    cur = root
    stack = []
    while stack or cur:
        if cur :
            stack.append(cur)
            cur = cur.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack[-1]
                stack.pop()
                print(temp.data,end=" ") 
                while stack and temp == stack[-1].right:
                    temp = stack[-1]
                    stack.pop()
                    print(temp.data,end=" ")
            else:
                cur = temp
# post_order_s1(root)
# using single stack pre,in,post -order traversal
def pre_in_post(root):
    pre = []
    in_list = []
    post = []
    stack = [(root,1)]
    while stack:
        node,num = stack.pop()
        if num ==  1:
            pre.append(node.data)
            num += 1
            stack.append((node,num))
            if node.left:
                stack.append((node.left,1))
        elif num == 2:
            in_list.append(node.data)
            num += 1
            stack.append((node,num))
            if node.right:
                stack.append((node.right,1))
        else:
            post.append(node.data)
    print("pre:",pre)
    print("In:",in_list)
    print("post:",post)
pre_in_post(root)