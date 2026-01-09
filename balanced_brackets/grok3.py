def is_balanced(brackets):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = dict(zip(closing, opening))
    
    for bracket in brackets:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if not stack:
                return "NO"
            top = stack.pop()
            if top != pairs[bracket]:
                return "NO"
    
    return "YES" if not stack else "NO"

N = int(input())
sequence = input().strip()

print(is_balanced(sequence))