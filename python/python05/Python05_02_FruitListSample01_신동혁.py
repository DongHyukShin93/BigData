#Python05_02_FruitListSample01_신동혁
answer = []
fruitCnt = []
while True :
	a=int(input("10이상의 수를 입력 하세요. [ Exit : 0]"))
	if 0 < a <10 :
		print("10이상의 숫자 확인 하세요.")		
	elif a==0 :
		break
	elif a>=10 :
		print('===<<%d번 반복합니다.>>==='%a)
		for i in range(1,a+1) :
			if i%3==0 :
				answer.append('Apple')
			if i%4==0 :
				answer.append('Melon')
			if i%5==0 :
				answer.append('Grape')
			if i%8==0 :
				answer.append('StrawBerry')
			fruitCnt += answer
			if len(answer)==0 :
				print("%d. "%i)
			else :
				print("%d. "%i, answer)
			answer = []
		print('==<< Fruit Counter List >>==')
		print('Apple : %d회' %fruitCnt.count('Apple'))
		print('Melon : %d회' %fruitCnt.count('Melon'))
		print('Grape : %d회' %fruitCnt.count('Grape'))
		print('StrawBerry : %d회 '%fruitCnt.count('StrawBerry'))