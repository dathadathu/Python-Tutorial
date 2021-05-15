n = int(input("Enter number of elements: \n"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)

def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

even, odd = count(lst)

print("Even : {} \n Odd : {}".format(even,odd))
