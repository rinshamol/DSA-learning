def areBracketsProperlyMatched(code_snippet):
    stack = []
    for ch in code_snippet:
    
        if (ch in "({["):
            stack.append(ch)
        elif ch in "]})":
            if not stack :
                return 0
            top = stack[-1]
            if (top == '(' and ch == ')') or (top == '[' and ch ==']') or (top == '{' or ch == '}'):
                stack.pop()
            else:
                return 0
    if not stack:
        return 1
    else :
        return 0
code_snippet = "if (a[0] > b[1]) { doSomething(); }"
print(areBracketsProperlyMatched(code_snippet))