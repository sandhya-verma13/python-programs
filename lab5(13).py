import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    # Calculate two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Roots:", root1, root2)
elif discriminant == 0:
    # Calculate two real and identical roots
    root = -b / (2*a)
    print("Roots:", root, root)
else:
    # Calculate two complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Roots: {} + {}i, {} - {}i".format(real_part, imaginary_part, real_part, imaginary_part))

