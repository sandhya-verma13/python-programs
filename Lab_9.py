                                        #Low

                                        
# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
n,d=map(int,input("Enter the two number : ").split())
try:
    r=n/d
    print(f"The division of {n} by {d} is : {r}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError!! {e}")

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
n=input("Enter the two number : ")
try:
    r=int(n)
    print(f"The Given number is int")
except ValueError :
    print(f"ValueError!!")
# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def num(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise TypeError("Input must be a numerical value")
try:
    num1 =num("Enter the first number: ")
    num2 =num("Enter the second number: ")
    print(f"The numbers you entered are {num1} and {num2}")
except TypeError as e:
    print(e)

#...........................................................................................................................................................

                                        #Medium
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def so(na):
    try:
        file = open(na, 'r')
        contents = file.read()
        print("File contents:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
name=input("Enter the file name :")
so(name)

# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def pos(lst,ind):
    try:
        k=lst[ind]
        print(f"The number at index {ind} is {k}")
    except IndexError:
        print(f"{ind} is out of range...")
lst=[2,5,7,1,2,9,7,0]
n=int(input("Enter the index position :"))
pos(lst,n)

#...........................................................................................................................................................

                                        # High
# Write a sample python program for handling multiple exceptions.
try:
    n1=int(input("Enter a number :"))
    n2=int(input("Enter a number :"))
    f=n1/n2
    print(f"The number {n1} divide by {n2} is ;{f}")
except (ZeroDivisionError,ValueError) as e:
    print(f"{e} Occureed...")


#...........................................................................................................................................................