def binary_search(items, value, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if value == items[middle]:
        return middle

    if (value < items[middle]):
        return binary_search(items, value, left, middle - 1) 

    return binary_search(items, value, middle + 1, right)

items = [-3, -1, 1, 3, 5, 7, 9, 11]

print(binary_search(items, 100, 0, len(items) - 1))
print(binary_search(items, -1, 0, len(items) - 1))
print(binary_search(items, 7, 0, len(items) - 1))