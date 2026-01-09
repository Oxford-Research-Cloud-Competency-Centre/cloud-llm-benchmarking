import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str or not n_str.strip():
            print("YES")
            return

        n = int(n_str)
        s = sys.stdin.readline().strip()

        if n == 0:
            print("YES")
            return

        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or mapping[char] != stack.pop():
                    print("NO")
                    return
            else:
                # According to the problem, only brackets will be present.
                # If other characters could appear, this would be an error.
                pass
        
        if not stack:
            print("YES")
        else:
            print("NO")

    except (ValueError, IndexError):
        # This can happen with malformed input, e.g., non-integer N.
        # A safe default for unexpected errors in this context is "NO".
        print("NO")

solve()