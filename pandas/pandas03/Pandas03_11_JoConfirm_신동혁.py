#Pandas03_11_JoConfirm_신동혁
import sys
import random

while True :
	nameList = []
	nameList = input("4인 이상의 이름을 입력하세요. (종료 : 0) ").split()
	if "0" in nameList :
		print("\n종료하겠습니다.", end="\n\n")
		break
	elif len(nameList) < 4 :
		print("\n인원수가 부족합니다. 다시 입력하세요", end="\n\n")
	else :
		rdnumList = [] # rdnumList를 15라인 while문 안에 넣어서 오류가 발생했다.
		while True :
			rdnum = random.randint(1,len(nameList))
			if rdnum not in rdnumList :
				rdnumList.append(rdnum)
			elif len(nameList) == len(rdnumList) :
				break
			else :
				continue
	# break #01. 여기서 break를 하면 25라인부터의 for문이 시작되지 않는다.
	print()
	for i in nameList : #01. break 쓰면 25라인부터의 for문을 while 문 밖으로 빼면 되는데, 그러면 input 반복 안함
		print(i, end="\t")
	print()
	for j in rdnumList :
		print(j, end="\t")
	print("\n")