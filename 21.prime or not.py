pn = int(input("Number please"))
for i in range(2,pn):
    if (pn%i) == 0:
        print(pn,"Not prime")
        break
else:
    print(pn,"prime")