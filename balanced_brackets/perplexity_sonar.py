def is_balanced_brackets(n, s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    open_set = set(pairs.values())

    for ch in s:
        if ch in open_set:
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop() != pairs.get(ch, None):
                return False
    return not stack


def main():
    import sys
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    n = int(data.strip())
    s = data[1].strip() if len(data) > 1 else ""
    if len(s) != n:
        s = s[:n]
    print("YES" if is_balanced_brackets(n, s) else "NO")


if __name__ == "__main__":
    main()