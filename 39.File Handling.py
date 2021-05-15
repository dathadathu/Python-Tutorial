f = open('Mydata','r')

print(f.readline(4),end="")

r = open('Mydata2','w')
r.write("Laptop")

r = open('Mydata2','a')
r.write("Mobile")

for data in f:
    r.write(data)

#other files should be read as rb and write as wb