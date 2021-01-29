arr = [6, 5, 4, 3, 2]


def recrusionCount(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop(0)
        return 1+recrusionCount(arr)


print(recrusionCount(arr))


# standard answer for author:
'''def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count(arr))'''
