words = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'
]

def in_words(words, word):
    first = 0
    last = len(words) - 1

    while(first <= last):
        middle = (first + last) // 2

        if word == words[middle]:
            return True

        if word < words[middle]:
            last = middle - 1

        else:
            first = middle + 1

    return False

print(in_words(words, 'four'))
print(in_words(words, 'nine'))