# def binarySearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if a[middle] == key:
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else :
#             start = middle + 1
#
#     return False

def binarySearch(a, left, right, key):
    if left > right:
        return -1
    middle = (left + right) // 2
    if a[middle] == key:
        return middle
    elif a[middle] > key:
        return binarySearch(a, left, middle-1, key)
    else:
        return binarySearch(a, middle+1, right, key)

key = 5
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, 0, len(data), key))