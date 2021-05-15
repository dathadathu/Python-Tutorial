#data types
#why so importants

#None
#numeric
#list
#tuple
#set
#string
#range
#dictionary

## NONE ## 
#not assigned to anything i.e., is null

## NUMERIC
    #int        - 10
    #float      - 10.5  
    #complex    - 9+6j
    num = 6+9j
    #bool       - T or F // 1 or 0

k = 6.3
b = 10
c = complex(b,k)

b<k

bool = k>b
type(bool)

int(True)
#1
int(False)
#0

"""
#Sequence 
-> list = []
-> tuple = ()
-> set = {}
-> String = 'navin',"tesluko"
-> range : used for iteration

"""
range(10)

list(range(10))

list(range(4,44,2))

list(range(100,1658654644,9))

#maping is also known as dictionary
d = {'Datha':'Samsung','Ram':'Realme','Achu':'íPhone','Charan':'OnePlus'}
d.keys()
d.values()

df = zip(d.keys(),d.values())

#help
print(help("str"))