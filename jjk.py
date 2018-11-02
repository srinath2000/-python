name={}
n=input("Enter the number of elements  :")
for i in range(n):
	roll_no=input("Enter the roll no :")
	name[roll_no]=raw_input("Enter the name  :")
print name
print "1.update "
print "2.search "
print "3.sort   "
print "4.delete "
ch=input("Enter the choice :")
if ch==1:
	new=input("Enter the roll no to be updated :")
	new1=raw_input("Enter the new name :")
	name[new]=new1
	print name
	
elif ch==2:
	sh=raw_input("Enter the name to be searched :")
	for j in name:
		if name[j]==sh:
			print "present"
			break
		else :
			print "not found"
		
elif ch==3:
	for v in sorted(name.values()):
		print v
else:
	del1=input("Enter the roll no to be deleted :")
	del name[del1]
	print name
