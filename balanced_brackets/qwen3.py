def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

n = int(input())
sequence = input().strip()

if is_balanced(sequence):
    print("YES")
else:
    print("NO")