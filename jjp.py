data_base={}
n=input("Enter the number of elements  :")
for i in range(n):
	acc=input("Enter the account no :")
	name=raw_input("Enter the name of the acc. holder :")
	bal=input("Enter the account balance :")
	data_base[acc]=[name,bal]
print data_base
print "1.credit "
print "2.debit "
print "3.balance  "

ch=input("Enter the choice :")
if ch==1:
	new1=input("Enter the account no :")
	new=input("Enter the amount to be credited  :")
	data_base[new1][1]+=new
	print data_base 
elif ch==2:
	new1=input("Enter the account no :")
	new=input("Enter the amount to be debited  :")
	data_base[new1][1]-=new
	print data_base 
else:
	new1=input("Enter the account no :")
	print data_base[new1][1]
	#print data_base 
	 
print name

