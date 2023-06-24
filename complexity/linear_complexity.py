def get_minimum(items):
    minimum = items[0]

    for i in range(len(items)):
        if minimum > items[i]:
            minimum = items[i]

    return minimum

def get_average(items):
    sum = 0

    for i in range(len(items)):
        sum += items[i]

    return sum / len(items)
    
items = [34, 3, 5, 67, 2, 36, 73, 25, 86, 33]

print(get_minimum(items))
print(get_average(items))