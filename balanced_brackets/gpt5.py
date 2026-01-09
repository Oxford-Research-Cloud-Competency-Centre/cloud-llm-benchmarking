import sys

def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opens = set(pairs.values())
    closes = set(pairs.keys())
    if len(s) % 2 == 1:
        return False
    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch in closes:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            return False
    return not stack

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1] if len(data) > 1 else ""
    print("YES" if is_balanced(s) else "NO")

if __name__ == "__main__":
    main()