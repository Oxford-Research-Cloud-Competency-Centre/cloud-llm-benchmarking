for char in s:
    if char in '([{':
        stack.append(char)
    else:  # char is one of ')]}'
        if not stack or stack.pop() != bracket_map[char]:
            print("NO")
            exit()

if not stack:
    print("YES")
else:
    print("NO")