#Python03_08_ForExp01_신동혁
a = [1,2,3,4]
result=[]
for num in a :
	result.append(num*3)
print(result)

print("="*40)

result=[num*3 for num in a]
print(result)