
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 != side2 and side1 != side3 and side2 != side3:
    print("This is a scalene triangle.")
elif side1 == side2 and side1 == side3:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")
