import sys

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    numbers = list(map(int, line.split()))
    numbers.sort()
    print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    main()