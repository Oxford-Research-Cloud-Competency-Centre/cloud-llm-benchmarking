def is_balanced(bracket_sequence):
    stack = []
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    open_brackets = bracket_map.keys()
    close_brackets = bracket_map.values()
    
    for bracket in bracket_sequence:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if not stack or bracket_map[stack.pop()] != bracket:
                return "NO"
    
    return "YES" if not stack else "NO"

def main():
    N = int(input().strip())
    bracket_sequence = input().strip()
    print(is_balanced(bracket_sequence))

if __name__ == "__main__":
    main()