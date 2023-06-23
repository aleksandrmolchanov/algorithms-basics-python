from datetime import datetime

def selection_sort(items):
    for i in range(len(items) - 1):
        index_min = i
        for j in range(i + 1, len(items) - 1):
            if items[j] < items[index_min]:
                index_min = j
        items[i], items[index_min] = items[index_min], items[i]

items = [86, 66, 44, 77, 56, 64, 76, 39, 32, 93, 33, 54, 63, 96, 5, 41, 20, 58, 55, 28]

start = datetime.now()
selection_sort(items)
end = datetime.now()
print(end - start)
