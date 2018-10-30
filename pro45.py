a=[]
n=input(" Enter the no of elements  :")
for i in range(1,n+1):
	v=input("Enter the number :")
	v=v**3
	a.append(v)
print a
pos=[]
neg=[]
zero=[]
for i in a:
	if i>0:
		pos.append(i)
		
	elif i<0:
		neg.append(i)
		
	else:
		zero.append(i) 
		
print pos
print len(pos)
print neg
print len(neg)
print zero
print len(zero)	
