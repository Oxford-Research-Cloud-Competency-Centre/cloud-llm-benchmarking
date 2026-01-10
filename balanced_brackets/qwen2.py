from collections import deque

def is_balanced(brackets):
    stack = deque()
    for bracket in brackets:
        if bracket in "([{":
            stack.append(bracket)
        else:
            if not stack:
                return "NO"
            if bracket == ")" and stack[-1] != "(":
                return "NO"
            elif bracket == "]" and stack[-1] != "[":
                return "NO"
            elif bracket == "}" and stack[-1] != "{":
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

# Read input
n = int(input())
brackets = input()

# Check if balanced
print(is_balanced(brackets))