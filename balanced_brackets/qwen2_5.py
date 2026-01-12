n = int(input())
s = input().strip()

stack = []

for char in s:
    if char in {'(', '[', '{'}:
        stack.append(char)
    else:
        if not stack:
            print("NO")
            exit()
        top = stack.pop()
        if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
            print("NO")
            exit()

print("YES" if not stack else "NO")