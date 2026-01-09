import sys

def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return "NO"
            if stack[-1] != matching[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    if n == 0:
        print("YES")
        return
    s = data[1]
    print(is_balanced(s))

if __name__ == "__main__":
    main()