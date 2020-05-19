def binary_search(element, some_list):
    l = 0
    r = len(some_list) - 1
    while l <= r:
        mid = (l + r) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            r = mid - 1
        else:
            l = mid + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
