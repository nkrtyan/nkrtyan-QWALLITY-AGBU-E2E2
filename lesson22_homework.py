def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def find_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def bubble_sort(numbers):
    sorted_list = numbers.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list


# Main
numbers = [23, 5, 67, 12, 89, 1, 45]

print("Original list:", numbers)
print("Maximum:", find_max(numbers))
print("Minimum:", find_min(numbers))
print("Sum:", calculate_sum(numbers))
print("Sorted list:", bubble_sort(numbers))
