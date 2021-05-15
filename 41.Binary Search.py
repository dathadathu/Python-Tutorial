"""
pos = -1
def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] > n:
                l = mid
            else:
                u = mid

    return False

list = [2,3,45,6,39,6,785,663,1564,5610154,1223,100]
n = 100

if search(list,n):
    print("Found", pos)
else:
    print("Not Found")

"""


#sorted
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9, 12, 14, 18, 22, 25, 1224]
x = 1224

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")