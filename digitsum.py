#program to find the sum of digits of a number :
n=input(" Enter a number  :")
s=0
while(n>0):
    r=n%10
    s=s+r
    n=n/10
print s
