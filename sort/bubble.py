def bubble_sort(items):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]

items = [4, 3, 56, 12, 38, 53, 12, 5, 3, 6, 3, 12]
bubble_sort(items)
print(items)