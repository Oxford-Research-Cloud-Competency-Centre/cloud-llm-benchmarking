def check_balanced(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0

n = int(input())
s = input().strip()

if check_balanced(s):
    print("YES")
else:
    print("NO")