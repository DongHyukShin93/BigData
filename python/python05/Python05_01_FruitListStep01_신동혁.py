#Python05_01_FruitListStep01_신동혁
while True :
	a=int(input("10이상의 수를 입력 하세요. [ Exit : 0]"))
	if 0 < a <10 :
		print("10이상의 숫자 확인 하세요.")		
	elif a==0 :
		break
	elif a>=10 :
		print('===<<%d번 반복합니다.>>==='%a)