# a=int(raw_input("give the value"))
# for i in range(2,a):
# 	if a%i==0:
# 		print "nahi"
# 		break
# else:
# 	print "hai"	
for x in range(2,10):
	for y in range(2,10):
		if x%y==0:
			print "nahi hai"+y
	else:
		print "hai"+y		
		