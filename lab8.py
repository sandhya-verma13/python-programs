 # low

# 1.Write a Python module for temperature conversions. Utilize those functions in another Python program.

#tem.py

def te(cel,fah):
    f= (cel* 1.8) + 32
    c = (fah - 32) / 1.8
    return f,c
 
#cal.py
import tem
cel= float(input("Enter the temperature in Celsius: "))
fah= float(input("Enter the temperature in Fahrenheit: "))
f,c=tem.te(cel,fah)
print(f"{cel:.2f} degrees Celsius is equal to {f:.2f} degrees Fahrenheit")
print(f"{fah:.2f} degrees Fahrenheit is equal to {c:.2f} degrees Celsius")

# 2.Write a Python module for currency conversion. Use that conversion functions in another Python program.

#convert.py

def con1(a):
 return a*83.36

#result.py

import convert
n=float(input("Enter a money in dollars :"))
k=convert.con1(n)
print(f"The Dollar in Rupees is : {k}")

#...................................................................................................................................................

 # medium

# 1.Generate a Python module which performs arithmetic operation. Import that module in another program which utilizes those operations.

#operation.py

def pro(a,b):
    return a+b,a-b,a*b,a/b,a//b

#main.py

import operation
n1,n2=map(int,input().split())
s,t,u,v,w=operation.pro(n1,n2)
print(f"Addition is {s}\nSubtraction is {t}\nMultiplication is {u}\nDivision is {v}\nFloor Division is {w}")

#...................................................................................................................................................

 # high

# 1.Write a Python module that converts decimal to binary and binary to decimal. Generate a Python program that imports the conversion module and utilizes those function.

#btod.py

def con1(n1,n2):
    m=''
    while n1!=0:
        m=str(n1%2)+m
        n1=n1/2
        m1=str(n2)
        l=0
        for i in range(0,len(m1)):
            l+=int(m1[i]*(2**(leb(m1)-i-1))
    return m,l

#main.py

import btod
b,d=map(int,input("Enter a decimal and binary number : ").split())
m1,m2=btod.con1(b,d)
print(f"The Decimal to Binary is :{m1}\nThe Binary to Decimal is :{m2}")

#...................................................................................................................................................


