#Python03_22_Chap03Practice_06_신동혁
numbers = [1, 2, 3, 4, 5]
result = []
for a in numbers :
	if a%2==1 :
		result.append(a*2)
print(result)

result = [a*2 for a in numbers if a%2==1]
print(result)