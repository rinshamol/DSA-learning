# using list
stack = []
def push (n):
    stack.append(n)
    print(stack)

def pop():
    if stack:
        stack.pop()
        print(stack)
    else:
        print("Stack is empty")

def top():
    if stack: 
         print(stack[-1])
    else:
        print("Stack is empty")
def size():
    return len(stack)

push(2)
push(3)
push(4)
push(5)
push(6)
pop()
pop()
top()
print(size())
