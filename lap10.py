# Read a number from input
n=int(input("Enter  how many number?"))
#Assing n1,n2
n1,n2=0,1
#Assing count variable
count=0
#check for fibonacci sequence
if(n<=0):
    printf("please Enter a positive integer")
elif(n==1):
    print("Fibonacci sequence upto:",n,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1



