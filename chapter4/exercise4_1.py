arr = [6, 5, 4, 3, 2, 1]
# print(len(arr))
#a = arr.pop(0)
# print(a)
# print(arr[len(arr)-1])
#b = arr
#print(a, b)


def recrusionSum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0)+recrusionSum(arr)


print(recrusionSum(arr))


# standard answer for author:
'''def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum(arr))'''
