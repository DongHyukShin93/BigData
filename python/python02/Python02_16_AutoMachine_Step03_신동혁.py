#Python02_16_AutoMachine_Step03_신동혁

menu = ["Orange","Strawberry","Peach","Mango","Grape"]
money = [1000,2500,1500,2000,2000]
print("***홍익 대학교 과일 판매머신 V02***")
print("\n")
for num in range(0,5) :
	if num == 0 :
		print(num+1,'. ',menu[num],"     : ",money[num],"원",sep="")
	elif num == 1 :
		print(num+1,'. ',menu[num]," : ",money[num],"원",sep="")
	else :
		print(num+1,'. ',menu[num],"      : ",money[num],"원",sep="")
print("6. 종료",sep="")
print("\n")
print("===================================")
print("\n")
while True :
	a=int(input("구매 번호를 입력하세요.(1~5)"))
	if a in range(1,6) :
		print(menu[a-1],"는", money[a-1],"원입니다.")
	elif a==6 :
		print("종료합니다.")
		break
	else :
		print("잘못된 입력입니다.")