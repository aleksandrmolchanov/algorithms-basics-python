def sort(items, direction = 'asc'):
    items_length = len(items)

    if items_length == 0:
        return []

    index = items_length // 2
    element = items[index]

    smaller_items = [
        items[i]
        for i in range(items_length)
        if items[i] < element and i != index
    ]
    bigger_items = [
        items[i]
        for i in range(items_length)
        if items[i] >= element and i != index
    ]

    sorted_smaller_items = sort(smaller_items, direction)
    sorted_bigger_items = sort(bigger_items, direction)

    if direction == 'asc':
        return [*sorted_smaller_items, element, *sorted_bigger_items]
    return [*sorted_bigger_items, element, *sorted_smaller_items]

items = [4, 57, 23, 73, 12, 89, 27, 54, 25, 1, 45, 43, 63, 78, 32, 43, 66]

print(sort(items))