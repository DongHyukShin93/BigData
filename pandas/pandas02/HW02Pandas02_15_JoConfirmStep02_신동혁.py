#HW02Pandas02_15_JoConfirmStep02_신동혁
import sys
import random

while True :
	nameList = []
	nameList = input("4인 이상의 이름을 입력하세요. (종료 : 0) : ").split() # split()을 넣은 이유가?
	if "0" in nameList  :
		print("\n종료합니다.", end="\n\n")
		break
	elif len(nameList) < 4 :
		print("\n인원 수가 부족합니다.", end="\n\n")
		 # continue가 왜 들어가요?
	else :
		rdNumList = [] # 힌트 : append() 사용
		while True :
			rdNum = random.randint(1,len(nameList))
			if rdNum not in rdNumList :
				rdNumList.append(rdNum)
			elif len(nameList) == len(rdNumList) :
				break
			else :
				continue # rdNumListd에서 숫자가 중복되지 않을 때까지 숫자를 뽑기위해 continue
		for i in nameList :
			print(i, end="\t")
		print()
		for j in rdNumList :
			print(j, end="\t")
		print("\n")
################## 이거 내가 한 거 아님 이해하자 ##########