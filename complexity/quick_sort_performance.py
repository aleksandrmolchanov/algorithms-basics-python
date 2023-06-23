from datetime import datetime

def quick_sort(items):
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

    def quick_sort(items, left, right):
        length = right - left + 1

        if length < 2:
            return

        pivot = items[left]
        split = partition(items, left, right, pivot)
        quick_sort(items, left, split - 1)
        quick_sort(items, split, right)

    quick_sort(items, 0, len(items) - 1)

items = [86, 66, 44, 77, 56, 64, 76, 39, 32, 93, 33, 54, 63, 96, 5, 41, 20, 58, 55, 28]
start = datetime.now()
quick_sort(items)
end = datetime.now()
print(end - start)