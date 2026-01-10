def is_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False
    return not stack

n = int(input())
s = input().strip()
if is_balanced(s):
    print("YES")
else:
    print("NO")