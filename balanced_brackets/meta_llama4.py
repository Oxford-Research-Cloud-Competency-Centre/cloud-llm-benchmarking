def is_balanced(n, brackets):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for bracket in brackets:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[bracket]:
                return "NO"

    return "YES" if not stack else "NO"


def main():
    try:
        n = int(input().strip())
        brackets = input().strip()
        if len(brackets) != n:
            raise ValueError
        print(is_balanced(n, brackets))
    except (ValueError, EOFError):
        # In a real application, you'd log this error
        pass


if __name__ == "__main__":
    main()