pos = -1
"""
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i = i + 1
    return False
"""

def search(list, n):
    #i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True

    return False

list = [2, 5, 6, 8, 9, 10, 13]
n = 13
if search(list,n):
    print("Found",pos)
else:
    print("Not Found")