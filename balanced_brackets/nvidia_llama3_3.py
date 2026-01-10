n = int(input().strip())
s = input().strip()

stack = []
mapping = {')': '(', ']': '[', '}': '{'}

valid = True
for char in s:
    if char in ['(', '[', '{']:
        stack.append(char)
    else:
        if not stack:
            valid = False
            break
        top = stack.pop()
        if mapping[char]!= top:
            valid = False
            break

if valid and not stack:
    print("YES")
else:
    print("NO")