#using Function
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
a,b=swap(a,b)
print("After swapping:")
print("a =", a)
print("b =", b)