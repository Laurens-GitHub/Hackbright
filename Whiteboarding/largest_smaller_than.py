# Given an ordered list of numbers and a number, return the index of the largest number in the list that is smaller than that number.

# For example:

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
# 2

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
# 4

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
# 1

def largest_smaller_than(list, number):
    largest = list[0]

    for idx, num in enumerate list:
        if num < number:
            largest = idx
        elif num > largest:
            largest = idx
        return largest

print(largest_smaller_than()
