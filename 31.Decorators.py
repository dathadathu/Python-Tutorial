def div(a,b):
    return a/b

div(5,8)

#decorators : can use the features from the others

def smart_div(func):

    def inner(a,b):

        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(5,8)
