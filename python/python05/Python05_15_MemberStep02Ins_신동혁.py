#Python05_14_MemberStep02Ins_신동혁
menu = ['1.  회원가입', '2.  로그인', '3.  회원목록', '9.  메뉴종료']
menuChk = ['1','2','3','9']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
memberCount=[] 
memberData=[]
print("{0:=^54}".format("메뉴선택"))
print()
for i in range(len(menu)) :
	print(menu[i], end="    ")
print("\n")
print("="*58)
while True :
	no = int(input("{0:>33}".format("메뉴의 번호를 선택해주세요.   ")))
	if no == 1 :
		print("Singup",end="\n\n")
		for i in range(len(itemList)) :
			memberData+=input("%s : " %itemList[i])
		memberCount.append(memberData)
		memberData=[]  # 왜 초기화를 시켜 주는지 이해하기
		print(memberCount)
		print("\n현재 회원수는 %d명입니다."%len(memberCount))
		print("\n")
	elif no == 2 :
		print("{0:^50}".format(menu[no-1]))
	elif no == 3 :
		print("{0:^50}".format(menu[no-1]))
	elif no == 9 :
		print("{0:^50}".format("종료합니다."))
		break
	
		'''
	for i in range(4) :
'''