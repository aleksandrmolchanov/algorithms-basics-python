def compare_by_price(a, b):
    if a["price"] < b["price"]:
        return -1
    elif a["price"] == b["price"]:
        return 0
    else:
        return 1
        
def compare_by_rating(a, b):
    if a["rating"] < b["rating"]:
        return -1
    elif a["rating"] == b["rating"]:
        return 0
    else:
        return 1

def bubble_sort(items, comparator):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if comparator(items[i], items[i + 1]) > 0:
                items[i], items[i + 1] = items[i + 1], items[i]

products = [
  {"name": "Toyota", "price": 100000, "rating": 9.1},
  {"name": "Volvo", "price": 20000, "rating": 8.3},
  {"name": "Honda", "price": 14000, "rating": 7.5},
  {"name": "Chevrolet", "price": 30000, "rating": 9.2},
  {"name": "Buick", "price": 200000, "rating": 8.7},
  {"name": "Pontiac", "price": 7000, "rating": 8.2},
  {"name": "Ford", "price": 20000, "rating": 9.0},
  {"name": "Dodge", "price": 80000, "rating": 7.8},
  {"name": "Cadillac", "price": 5000, "rating": 7.1},
]

bubble_sort(products, compare_by_price)
print(products)

bubble_sort(products, compare_by_rating)
print(products)
