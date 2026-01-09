import sys

def main():
    input_data = sys.stdin.read()
    integers = list(map(int, input_data.split()))
    integers.sort()
    print(" ".join(map(str, integers)))

if __name__ == "__main__":
    main()