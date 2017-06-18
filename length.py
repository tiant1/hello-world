# conding: utf-8
a = int(input("Enter length of a: "))
b = int(input("Enter length of b: "))
c = (a**2 + b**2) ** (1/2)
def cl(a,b):
    return c

print("length of c:", cl(a,b))