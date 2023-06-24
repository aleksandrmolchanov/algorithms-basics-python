from datetime import datetime

def selection_sort(items):
    for i in range(len(items) - 1):
        index_min = i
        for j in range(i + 1, len(items) - 1):
            if items[j] < items[index_min]:
                index_min = j
        items[i], items[index_min] = items[index_min], items[i]


def average_performance(f, count):
    start = datetime.now()

    for i in range(count):
        f

    end = datetime.now()

    return (end - start) / count

items = [86, 66, 44, 77, 56, 64, 76, 39, 32, 93, 33, 54, 63, 96, 5, 41, 20, 58, 55, 28]

print(average_performance(selection_sort(items[:]), 1)) 
print(average_performance(selection_sort(items[:]), 10)) 


