import sys

def is_balanced(s):
    stack = []
    opening = '([{'
    closing = ')]}'
    matches = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != matches[char]:
                return "NO"
    return "YES" if not stack else "NO"

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])
s = data[1]
print(is_balanced(s))