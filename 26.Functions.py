def add(b, a):
    return a + b


a = 24
b = 45
c = add(5, 6)
print(c)


# pass by value
# pass by reference

def update(x):
    print(id(x))

    x = 8
    print(id(x))
    print("x", x)


a = 10
print(id(a))
update(a)
print("a", a)


def up(tup):
    print(id(tup))

    tup[1] = 8
    print(id(tup))
    print("tup", tup)


tup = [2, 5, 6, 3, 1]
print(id(tup))
up(tup)
print("tup", tup)

def mul(c,d):
    m = c*d
    print(m)

mul(5,6)
#position argument


#keyword argument

#default argument

def person(name,age = 18):
    print(name)
    print(age)

person(age=24, name="Prasuuu")

person("Prasuu",24)

#variable length argument
def sum(*b):
    c = 0
    for i in b:
        c = c+i

    print(c)

sum(60,80,70,10)

#keyword variable length argument


def per(name, **data):

    print(name)
    print(data)



per('Shiva Datha',age = 28,city = 'Sangareddy',Phone = 9441490877)

def per2(name, **data):

    print(name)
    for i,j in data.items():
        print(i,j)



per2('Shiva Datha',age = 28,city = 'Sangareddy',Phone = 9441490877)


p = 10
print(id(p))
def something():
    global p
    p = 15
    print("in function", p)
    print(id(p))

    p = 9

something()

print("outside", p)
print(id(p))
