def selection_sort(items):
    for i in range(len(items) - 1):
        index_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[index_min]:
                index_min = j
        items[i], items[index_min] = items[index_min], items[i]

items = [4, 3, 56, 12, 38, 53, 12, 5, 3, 6, 3, 12]
selection_sort(items)
print(items)