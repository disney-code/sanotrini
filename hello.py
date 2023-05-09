print("hello charlene")

def summation(a,b):
    return a+b

def product(a,b):
    return a*b

def divisionNewBranch(a,b):
    return a/b
a=int(input("enter a number: "))
b=int(input("second nnumber: "))
c=summation(a,b)
print("the summation of is ", c)
print(f"the product of {a} * {b} is",product(a,b))
temp1=divisionNewBranch(a,b)
print(f"{a}/{b} is ", temp1)
