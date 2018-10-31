#salary=(10000,71000,6589,452638,92392,2346,1000,63738,64333,8999)
salary=(1,2,3)
print salary
print max(salary)
print min(salary)
s=0
for i in salary:
	s=(s+i)/(len(salary))
print s

'''def area(r):
	areac=3.14*r*r
	circum=2*3.14*r
	return (areac,circum)

(x,y)=area(1)
print x,y'''
