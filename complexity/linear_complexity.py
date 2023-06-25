import math

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
    

def is_prime(number):
    if number < 2:
        return False

    sqrt = math.sqrt(number)
    for i in range(2, int(sqrt)):
        if number % i == 0:
            return False

    return True


items = [34, 3, 5, 67, 2, 36, 73, 25, 86, 33]

print(get_minimum(items))
print(get_average(items))
print(is_prime(7))