numbers = input().split()
numbers = [int(x) for x in numbers]
numbers.sort()
print(' '.join(map(str, numbers)))