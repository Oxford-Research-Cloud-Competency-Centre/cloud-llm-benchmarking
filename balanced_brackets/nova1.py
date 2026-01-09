def is_balanced(sequence):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for bracket in sequence:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if not stack or stack[-1]!= bracket_map[bracket]:
                return "NO"
            stack.pop()
    
    return "YES" if not stack else "NO"

n = int(input())
sequence = input().strip()
print(is_balanced(sequence))