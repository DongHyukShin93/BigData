#Python02_20_AutoMachine_Step05_신동혁
menu = ["Orange","Strawberry","Peach","Mango","Grape"]
money = [1000,2500,1500,2000,2000]
print("***홍익 대학교 과일 판매머신 V02***")
print("")
for num in range(0,5) :
	if num == 0 :
		print("%d. %s     : %d원" %(num+1, menu[num], money[num]))
	elif num == 1 :
		print("%d. %s : %d원" %(num+1, menu[num], money[num]))
	else :
		print("%d. %s      : %d원" %(num+1, menu[num], money[num]))
print("6. 종료")
print("="*35)
while True :
	coin=int(input("코인을 투입하세요."))
	print("투입된 금액은 %d원입니다."%coin)
	if coin > 0 :
		break
while True :
	a=int(input("구매 번호를 입력하세요.(1~5)"))
	if a in range(1,6) :
		print("선택한 과일은 %s이고, %s원입니다. " %( menu[a-1] , money[a-1] ))
		print("받은 금액은 %d원입니다."%coin)
		if coin >= money[a-1] :
			print("거스름돈은 %d원입니다."%(coin - money[a-1]))
			print("거스름돈 받아가시고, 과일 맛있게 드세요!")
			break
		else :
			print("금액이 부족합니다. 확인 바랍니다.")
			while True :
				coin=int(input("코인을 투입하세요."))
				print("투입된 금액은 %d원입니다."%coin)
				if coin > 0 :
					break
	elif a==6 :
		print("종료합니다.")
		break
	else :
		print("번호 확인 바랍니다.")