#Python02_17_AutoMachine_Step04_신동혁
menu = ["Orange","StrawBerry","Peach","Mango","Grape"]
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
print("6. 종료",sep="")
print("="*35)
while True :
	a=int(input("구매 번호를 입력하세요.(1~5)"))
	if a in range(1,6) :
		print("%s는 %d원입니다."%(menu[a-1],money[a-1]))
	elif a==6 :
		print("종료합니다.")
		break
	else :
		print("잘못된 입력입니다.")