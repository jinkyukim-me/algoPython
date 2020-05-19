# Use : for statement
# Don't use : append, insert, del

# function which return reverse of a string
# def is_palindrome(word):
#     reversedWord = word[::-1]
#     if reversedWord == word:
#         return True
#     return False

# function to check string is palindrome or not
def is_palindrome(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))