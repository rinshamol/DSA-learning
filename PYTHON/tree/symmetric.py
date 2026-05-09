class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)

root.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)

root.right.right = TreeNode(4)
root.right.right.left = TreeNode(6)


def symmetry(node):
    return not root or symmetric_check(root.left,root.right)
        
def symmetric_check(left, right):
    if not left or not root:
        return left == right
    if left.data != right.data:
        return False
    return symmetric_check(left.left,right.right) and symmetric_check(left.right,right.left)
print(symmetry(root))