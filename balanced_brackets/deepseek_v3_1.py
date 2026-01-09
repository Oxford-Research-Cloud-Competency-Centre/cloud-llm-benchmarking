def main():
    n = int(input().strip())
    s = input().strip()
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                print("NO")
                return
        else:
            print("NO")
            return
    print("YES" if not stack else "NO")

if __name__ == "__main__":
    main()