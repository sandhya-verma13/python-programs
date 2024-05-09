#1.QUESTION:

num=[1,2,3,4,5,6,7,8,9,10]
ev=[]
ev_sq=[]
odd=[]
od_sq=[]
for i in num:
  if i%2==0:
    ev.append(i)
    ev_sq.append(i*i)
  else:
    odd.append(i)
    od_sq.append(i*i)
print(ev)
print(ev_sq)
print(odd)
print(od_sq)

#2.QUESTION:
n=[]
e=int(input("Enter how many elements you want : "))
print("Enter",e,"numbers")
for i in range(e):
    num=int(input())
    n.append(num)
l=0
s=n[0]
for num in n:
    if num > l:
        l= num
    elif num<s:
        s=num
print("Largest number = ",l)
print("Smallest number = ",s)

#3.QUESTION:

n=[23,41,56,78,12,90]
fl=0
sl=0
fs=n[0]
ss=n[0]
for i in range(len(n)):
  if fl<n[i]:
    fl=n[i]
  elif fs>n[i]:
    fs=n[i]
for i in range(len(n)):
  if fl>n[i] and sl<n[i]:
    sl=n[i]
  elif fs<n[i] and ss>n[i]:
    ss=n[i]
print("Fist Largest = ",fl)
print("Second Largest = ",sl)
print("First Smallest = ",fs)
print("Second Smallest = ",ss)

#4.QUESTION: n=[5,3,7,9,8,4,2]
for i in range(len(n)):
  for j in range(len(n)):
    if n[i]<n[j]:
      temp=n[i]
      n[i]=n[j]
      n[j]=temp
print("Ascending order = ",n)
for i in range(len(n)):
  for j in range(len(n)):
    if n[i]>n[j]:
      temp=n[i]
      n[i]=n[j]
      n[j]=temp
print("Dscending order = ",n)

#5.QUESTION:
a=int(input("Enter how many elements u r gonin to Enter : "))
l=[]
f=0
for i in range(a):
  b=int(input(f"Enter the element {i+1} : "))
  l.append(b)
print(l)
k=int(input("for which number u need to find the index : "))
for i in range(a):
  if(k==l[i]):
    print("The index of the value",k,"is",i)
    f=1
    break
  else:
    f=0
if(f==0):
  print("value not found :(")

#6.QUESTION:

a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]
m_f_e = None
max_count = 0
for i in a:
    count = a.count(i)
    if count > max_count:
        m_f_e = i
        max_count = count
print("The most frequent element is:", m_f_e)


#7.QUESTION:

d={}
l1=[]
l2=[]
for i in range(3):
  a=input("Enter the key : ")
  l1.append(a)
for i in range(3):
  b=int(input("Enter the value : "))
  l2.append(b)
for i in range(3):
  d[l1[i]]=l2[i]
print(d)

#8.QUESTION:

a=["A","B","C","n"]
c=[0,0,0,0]
v=['a','b','c','d','e','f','g','h','i','j']
aa=[]
bb=[]
cc=[]
n=[]
bruh=[aa,bb,cc,n]
print("To vote A press 1\nTo vote B press 2\nTo vote C press 3\nTo vote none press 4")
for i in v:
  w=int(input(f"Please make ur vote {i} :"))
  if(w==1):
    aa.append(i)
    c[0]+=1
  elif(w==2):
    bb.append(i)
    c[1]+=1
  elif(w==3):
    cc.append(i)
  elif(w==4):
    n.append(i)
  else:
    print("Make sure u Enter crt option next time :)")
m=0
for i in range(4):
  if(m<c[i]):
    m=c[i]
for i in range(4):
  if(m==c[i]):
    print("The winner is",a[i],"with",c[i],"votes")
    print(bruh[i])
    c[i]=0
    break
sm=0
for i in range(4):
  if(sm<c[i]):
    sm=c[i]
for i in range(4):
  if(sm==c[i]):
    print("The Runner is",a[i],"with",c[i],"votes")
    print(bruh[i])
#9.QUESTION:

def menu():
  print("1.To convert dollars to rupees\n2. To convert celcius to fahrenheit\n3. To check your BMI\n4. To calculate Simple interest\nTo exit press 5")
  a=int(input("Enter your option :"))
  if(a==1):
    id()
  elif(a==2):
    cf()
  elif(a==3):
    bmi()
  elif(a==4):
    si()
  elif(a==5):
    print("Exited")
  else:
    print("Enter a Valid option :)")
    menu()
def id():
  a=int(input("Enter money value in dollars :"))
  print("In Indian rupees its",a*83.51)
  menu()
def cf():
  a=int(input("Enter the celcius : "))
  f=(a*(9/5)) + 32
  print("Fahrenheit is",f)
  menu()
def bmi():
  a=float(input("Enter ur weight"))
  b=float(input("Enter ur height"))
  bmi=a/(b*b)
  if(bmi<=18.4):
    print("underweight")
  elif(bmi<=24.9):
    print("normal")
  elif(bmi<=39.9):
    print("overweight")
  elif(bmi<=40):
    print("obese")
  menu()
def si():
  p=int(input("Enter the p  : "))
  r=int(input("Enter the r  : "))
  t=int(input("Enter the t  : "))
  prt=(p*r*t)/100
  print("The simple interest is",prt)
  menu()
menu()

#10.QUESTION:

a=int(input("Enter how many elements u r gonin to Enter : "))
l=[]
for i in range(a):
  b=int(input(f"Enter the element {i+1} : "))
  l.append(b)
for i in range(a):
  for j in range(a):
    if(l[i]<l[j]):
      temp=l[i]
      l[i]=l[j]
      l[j]=temp
print(l)


