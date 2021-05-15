#Errors
"""
1.Compile time - Syntax errors
2.Logical - wrong output
3.Run time - Ex: divide by zero.

"""
a = 5
b = 2
# noinspection PyBroadException

try:
    print("resource open")
    k = int(input("Enter the value:"))
    print(a/b)
    print("")
except ZeroDivisionError as e:
    print("Cannot divide number by Zero \n",e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong")
finally:
    print("resource closed")