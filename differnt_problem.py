# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

try:
    x = int(input(" enter a number "))
    print(type(x))
    y = x**2
    z = x**3
    comput = (x+y+z)
    print(comput)
except:
    print("please enter a number  not string ")