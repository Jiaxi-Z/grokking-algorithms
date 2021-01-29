arr = [5, 6, 9, 7, 4, 2]


def findMax(arr):

    if len(arr) == 1:
        max = arr.pop(0)
        return max
    else:
        sub_max = findMax(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max
        # return arr[0] if arr[0] > sub_max else sub_max


print(findMax(arr))

# standard answer for author:
'''def max(list):
    if len0(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max(arr))'''
