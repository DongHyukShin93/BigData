#HW02Pandas02_11_JoConfirmStep01_신동혁
'''
memberList = [] 
while True :
	memberList += str(input("4인 이상의 이름을 입력하세요."))
	if len(memberList) >= 4 :
		for i in range(len(memberList)) :
			print("%s 입력되었습니다." %memberList[i], end=" ")
'''
while True :
	nameList = []
	nameList = input("4인 이상의 이름을 입력하세요. (종료 : 0) : ").split() # split()을 넣은 이유가?
	if "0" in nameList  :
		print("종료합니다.")
		break
	elif len(nameList) < 4 :
		print("인원 수가 부족합니다.")
		#continue # continue가 왜 들어가요?
	else :
		for i in nameList :
			print(i, end=" ")
		print("총 %d명 입력되었습니다." % len(nameList))