n = int(input())
s = input()

stack = []
matching = {'(': ')', '[': ']', '{': '}'}

for char in s:
    if char in matching:
        stack.append(char)
    else:
        if not stack or matching[stack[-1]] != char:
            print("NO")
            exit()
        stack.pop()

if stack:
    print("NO")
else:
    print("YES")