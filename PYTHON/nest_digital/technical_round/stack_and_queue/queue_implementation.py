from collections import deque
queue = deque()
def push(n):
    queue.append(n)
    print(queue)

def pop():
    queue.popleft()
    print(queue)
def top():
    if queue:
        print(queue[0])
    else:
        print("queue is empty")
def size():
    print(len(queue))

push(1)
push(2)
push(3)
push(4)
top()

pop()
pop()
pop()
size()