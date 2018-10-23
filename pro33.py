sent_1=raw_input("Enter a string  :\n")
w=" "
for x in sent_1:
	if(x=='a'or x=='e'or x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U'):
		continue
	else:
		w=w+x
print "The edited string is :",w
w=sent_1.upper()
print "The edited string is :",w
sub=raw_input("Search")
w2=sent_1.find(sub)
print sub,"is present at the position",w2
sub1=raw_input("count")
w3=sent_1.count(sub1)
print "occurence=",w3
