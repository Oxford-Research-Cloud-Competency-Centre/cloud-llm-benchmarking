def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs.get(ch, ''):
                return False
            stack.pop()
    return not stack


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        print("YES")
        return
    if len(data) >= 2:
        s = data[1]
    else:
        s = ""
    print("YES" if is_balanced(s) else "NO")


if __name__ == "__main__":
    main()