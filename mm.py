a=[1,2,3,4,4,5,6,7,8]
max=0
b=0
while b<len(a):
	if max<a[b]:
		max=a[b]
	b+=1
print max		