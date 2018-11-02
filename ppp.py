stock={}
n=input("Enter the number of elements  :")
for i in range(n):
	n=raw_input("Enter the  item  :")
	stock[n]=0
print stock
for j in stock:
	if j=="pencil":
		stock[j]=input("Enter the number of pencils  :")
	elif j=="pen":
		stock[j]=input("Enter the number of pens :")
	elif j=="eraser":
		stock[j]=input("Enter the number of erasers :")
	else:
		stock[j]=input("Enter the number of ink bottles :")

print "1.print the dictionary"
print "2.remove the requested item"
print "3.add new stock for a particular item"
print "4.key value pairs"
ch=input("Enter the choice")
if ch==1:
	print stock
elif ch==2:
	el=raw_input("Enter the element to be removed  :")
	del stock[el]
	print stock
elif ch==3:
	new=raw_input("Enter the item with new stock :")
	new1=input("Enter the new quantity :")
	stock[new]=new1
	print stock
else:
	print stock.items()

