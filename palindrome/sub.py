def is_palindrome(word):
    for i in range(0, len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

print(is_palindrome("start"))
print(is_palindrome("mal2lam"))
print(is_palindrome("hello"))
print(is_palindrome("mydadym"))
