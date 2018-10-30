a=[]
n=input("Enter the no of names :")
for i in range (1,n+1):
	v=raw_input("Enter the name :")
	a.append(v)
old_1=raw_input("Enter the element to be replaced  :")
new_1=raw_input("Enter the  new element :")
for index,i in enumerate(a):
	if (i==old_1):
		a[index]=new_1
		print a
pos_1=input("Enter the index value :")
index=pos_1
del a[pos_1]
print a
del_1=raw_input("Enter the element to be deleted  :")
for i, index in enumerate(a):
	if(del_1==index):
		del a[i]
print a
