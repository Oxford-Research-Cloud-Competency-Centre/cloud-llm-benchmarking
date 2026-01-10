import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        right = []
        middle = []
        for num in arr:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        return quick_sort(left) + middle + quick_sort(right)

input_str = input("Enter a list of integers separated by spaces: ")
input_list = [int(num) for num in input_str.split()]
sorted_list = quick_sort(input_list)
print("Sorted list:", sorted_list)