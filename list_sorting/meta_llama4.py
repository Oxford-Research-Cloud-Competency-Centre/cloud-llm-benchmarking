import sys

def main():
    try:
        numbers = list(map(int, sys.stdin.readline().strip().split()))
        numbers.sort()
        print(' '.join(map(str, numbers)))
    except Exception as e:
        sys.stderr.write(f"An error occurred: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()