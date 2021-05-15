def topTen():

    n = 1

    while n <= 10:
        sq =n*n
        yield sq
        n += 1





val = topTen()
print(val.__next__())

for i in val:
    print(i)