menu = ['1. 탈퇴학생 ', '2. 추가등록 ', '3. 학생목록 ', '4. 합격생목록 ','9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
menuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []

for i in range(len(idList)) :
        dic[idList[i]] = scoreList[i]
while True :
	delid = input("탈퇴하고 싶은 ID를 입력하세요. (탈퇴하면 재가입할 수 없습니다.)  ")
	if delid not in idList :
		print()
		print("ID가 없습니다. 다시 입력하세요. ", end="\n\n")
		continue
	else :
		idList.remove(delid)
		deleteIDList.append(delid)
		del dic[delid]
		print()
		print("%s가 삭제되었습니다." %delid, end="\n\n")
	signid = input("등록할 ID를 입력하세요.  ")
	if signid in idList :
		print()
		print("이미 가입된 회원입니다. ", end="\n\n")
	elif signid in deleteIDList :
		print()
		print("탈퇴한 회원은 재가입할 수 없습니다.", end="\n\n")
	else :
		print("    ID : %s" %signid) # 여기서 input을 사용하면 탈퇴한 ID 입력이 가능해진다. print를 써도 달라지는 건 없는데...
		input("{:>9}".format("  PWD : "))
		input(f"{'PHONE : ':>9s}") # f 다음에 "{}"이면 {}안에는 "{''}", 반대로 '{}'라면 '{""}'
		input("{:>9}".format("EMAIL : "))
		print()
		print("회원가입이 완료되었습니다. 환영합니다!", end = "\n\n")