from collections import deque, defaultdict
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.left.left = TreeNode(6)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)
k = 2
n = root.left
def mark_parent(root, parents):
    que = deque([root])
    while que:
        cur = que.popleft()
        if cur.left:
            parents[cur.left] = cur
            que.append(cur.left)
        if cur.right:
            parents[cur.right] = cur
            que.append(cur.right)

def distance_calc(root, k, n):
    parents = defaultdict(int)
    mark_parent(root,parents)
    visited = defaultdict(bool)
    visited[n] = True
    que = deque([n])
    level = 0
    while que:
        size = len(que)
        
        if level == k: break
        for i in range(size):
            cur = que.popleft()
            if cur.left and not visited[cur.left]:
                que.append(cur.left)
                visited[cur.left] = True
            if cur.right and not visited[cur.right]:
                que.append(cur.right)
                visited[cur.right] = True
            if parents[cur] and not visited[parents[cur]]:
                que.append(parents[cur])
                visited[parents[cur]] = True
        level += 1
    while que:
        a = que.popleft()
        print(a.data,end=" ")
distance_calc(root,k,n)