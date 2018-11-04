#program to print the fibonocci series
n=input("Enter the limit  :")
x1=0
x2=1
counter=1
print x1,x2
while (counter<=n-2):
    xt=x1+x2
    print xt
    x1=x2
    x2=xt
    counter =counter+1
