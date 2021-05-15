arr = [20,65,19,62,410,9,312]
#n= 62

def sort(arr):

    for i in range(len(arr)):
        swapped = True

        for j in range(0,len(arr)-i-1):

            if arr[j] > arr[j + 1]:

                (arr[j],arr[j+1]) = (arr[j+1],arr[j])
                swapped = False

        if swapped:
            break

sort(arr)





if sort(arr,n):
    print("Found")
else:
    print("Not Found")