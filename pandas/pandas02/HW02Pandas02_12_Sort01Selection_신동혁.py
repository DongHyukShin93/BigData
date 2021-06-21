#HW02Pandas02_12_Sort01Selection_신동혁
sortNum = [2,5,6,1,2,8,33,77,12]     # outer for문과 inner for문의 range 범위에 대해 이해하기
for i in range(len(sortNum)-1) : # 예를 들어 77(마지막에서 첫번째)와 12(마지막)은 비교할 필요가 없기 때문에
	for j in range(i+1,len(sortNum)) :
		if sortNum[i] > sortNum[j] :
			temp = sortNum[i] # 여기 다른 변수(예 : temp)를 쓰지 않고 python에서는 a, b = b, a 같이 간단하게 교환할 수 있다.
			sortNum[i] = sortNum[j]
			sortNum[j] = temp
	print("%d회차 : " %(i+1), end=' ')
	for k in sortNum :
		print(k, end=' ')
	print()
#print(sortNum)