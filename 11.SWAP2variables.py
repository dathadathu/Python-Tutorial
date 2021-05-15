a = 5 
b = 6


print(a)
print(b)

#swap using 3rd variable

temp = a
a = b
b = temp

#swaping using 2 variables
a = a+b
b = a-b
a = a-b


#xor ^ : the advantage of xor is won't waste memory
a = a^b
b = a^b
a = a^b

print(a)
print(b)

a,b = b,a