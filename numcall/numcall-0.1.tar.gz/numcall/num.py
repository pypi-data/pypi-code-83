# Python program to convert a list to string
	
# Function to convert
def listToString(s):
	
	# initialize an empty string
	str1 = ""
	
	# traverse in the string
	for ele in s:
		str1 += str(ele)
	
	# return string
	return str1
		
		


def numcall(limit):
	# print('Press enter key to start')
	mob=[]
	for i in range(limit):
		q=str(input('')) #Enter now input
	
		for k in range(10):
			if len(q) == k:
				print(k)
				mob.append(k)
		i=i+1
	mobile=listToString(mob)
	print('The mobile number is : '+ mobile)


numcall(10)