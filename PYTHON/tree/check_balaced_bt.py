class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# # Manual balanced structure
# root = Node(10)

# # Level 1
# root.left = Node(5)
# root.right = Node(15)

# # Level 2 (filling both sides equally)
# root.left.left = Node(2)
# root.left.right = Node(7)
# root.right.left = Node(12)
# root.right.right = Node(20)

# Manual unbalanced structure (Right-Skewed)
root = Node(10)

# Every node only gets a right child
root.right = Node(20)
root.right.right = Node(30)
root.right.right.right = Node(40)
root.right.right.right.right = Node(50)

# check for balanced binary tree
def check(node):
    if not node:
        return 0
    l = check(node.left)
    if l == -1:
        return -1
    r = check(node.right)
    if r == -1:
        return -1
    if abs(r-l) > 1:
        return -1
    return 1+max(l,r)
print(check(root))