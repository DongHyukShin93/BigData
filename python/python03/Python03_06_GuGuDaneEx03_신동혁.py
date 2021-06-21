#Python03_06_GuGuDaneEx03_신동혁
for i in range (2,4) :
	print("outer",end=" ")
	print(i)
	'''
	print ("inner",end=" ")
	'''
	for j in range(1,5) :
		print ("inner", j , end="\t")
	print("")