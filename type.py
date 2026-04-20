a = int(input("enter first side's length: "))
b = int(input("enter second side's length : "))
c = int(input("enter third side's length: "))

if (a == b == c):
    print("the triangle is equilateral")
elif (a == b )or (b == c )or (c == a):
    print("the triangle is isosceles")
else:
    print("the triangle is scalene")
