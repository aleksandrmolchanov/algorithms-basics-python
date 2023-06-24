def palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

print(palindrome(''))
print(palindrome('a'))
print(palindrome('ab'))
print(palindrome('aba'))
print(palindrome('abba'))