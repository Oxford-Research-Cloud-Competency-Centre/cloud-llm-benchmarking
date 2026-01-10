def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '[':
            stack.append(char)
        elif char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        elif char == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
        elif char == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

for _ in range(int(input())):
    s = input()
    print(is_balanced(s))