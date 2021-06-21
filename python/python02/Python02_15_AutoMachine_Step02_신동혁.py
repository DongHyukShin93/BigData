#Python02_15_autoMachine_Step02_신동혁
menu = ["Orange","Strawberry","Peach","Mango","Grape","종료"]

print("***홍익 대학교 과일 판매머신 V02***")
print(" ")
for num in range(0,6) :
	print(num+1,'.',menu[num])
print(" ")
print("===================================")
print(" ")
while True :
	a=int(input("구매 번호를 입력하세요.(1~5)"))
	if a==1 :
	    print("Orange는 1,000원입니다.")
	elif a==2 :
	    print("Strawberry는 2,500원입니다.")
	elif a==3 :
	    print("Peach는 1,500원입니다.")
	elif a==4 :
	    print("Mango는 2,000원입니다.")
	elif a==5 :
	    print("Grape는 2,000원입니다.")
	elif a==6 :
		print("종료합니다.")
		break
	else :
		print("잘못된 입력입니다.")