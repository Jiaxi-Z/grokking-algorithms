def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2  # int((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    # return guess


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))  # 0
print(binary_search(my_list, 3))  # 1
print(binary_search(my_list, 5))  # 2
print(binary_search(my_list, 7))  # 2
print(binary_search(my_list, 9))  # 4

print(binary_search(my_list, -1))  # None
print(binary_search(my_list, 2))  # None
print(binary_search(my_list, 10))  # None
