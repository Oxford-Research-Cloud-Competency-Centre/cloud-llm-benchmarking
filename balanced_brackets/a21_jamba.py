def is_balanced(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
        elif char in matching.values():
            stack.append(char)
    return not stack

n = int(input())
s = input()
result = "YES" if is_balanced(s) else "NO"
print(result)