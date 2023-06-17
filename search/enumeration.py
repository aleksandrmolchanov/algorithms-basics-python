words = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'
]

def in_words(words, word):
    for i in range(len(words)):
        if words[i] == word:
            return True
    return False

print(in_words(words, 'four'))
print(in_words(words, 'nine'))