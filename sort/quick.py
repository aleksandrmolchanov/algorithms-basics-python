def partition(items, left, right, pivot):
    while True:
        while items[left] < pivot:
            left += 1
        
        while items[right] > pivot:
            right -= 1

        if left >= right:
            return right + 1

        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1


def sort(items, left, right):
    length = right - left + 1

    if length < 2:
        return

    pivot = items[left]
    split = partition(items, left, right, pivot)
    sort(items, left, split - 1)
    sort(items, split, right)

def quicksort(items):
    sort(items, 0, len(items) - 1)

items = [45, 12, 6, 37, 54, 94, 36, 58, 65, 15, 43, 64, 32]
quicksort(items)
print(items)