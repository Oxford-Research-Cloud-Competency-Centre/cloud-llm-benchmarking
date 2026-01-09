def is_balanced(s):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    open_brackets = set(["(", "{", "["])

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return "NO"
        else:
            return "NO"

    if not stack:
        return "YES"
    else:
        return "