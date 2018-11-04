#program to find the reverse of a number :
n=input("Enter a number :")
rev_n=0
n1=n
while(n>0):
    r=n%10
    rev_n=rev_n*10+r
    n=n/10
    n1-=1
print rev_n
