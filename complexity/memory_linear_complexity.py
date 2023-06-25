def remove_duplicates(items):
    visited = set()
    i = 0
    while i < len(items):
        if items[i] in visited:
            items.pop(i)
        else:
            visited.add(items[i])
            i += 1

items = [2, 34, 23, 24, 34, 6, 7, 7, 34, 5]

remove_duplicates(items)
print(items)