a=[2,5,8,9,8,9,2,3,4,6,5,6,5]

for i in len(a):
	for x in range(1,len(a)):
		if a[i]==a[x]:
			print x
		else:
			print ''	