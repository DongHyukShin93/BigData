#Python06_12_StudentMS_Step02_v00_신동혁
menu = [' 탈퇴학생 ', ' 추가등록 ', ' 학생목록 ', ' 합격생목록 ',' 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
menuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;

for i in range(len(idList)) :
	dic[idList[i]] = scoreList[i]

print("-"*80)
print("{0:^68}".format("학생 관리 시스템v01"))
print("-"*80)
for i in range(len(menu)) :
	print("%s. %s" %(menuChk[i], menu[i]), end="\t")
print()
print("-"*80)
while True :
	num = int(input("번호 입력 : "))
	print()
	if num == int(menuChk[4]) :
		print("학생 관리 시스템을 종료합니다.", end="\n\n")
		break
	elif num == int(menuChk[0]) :
		print("탈퇴 학생", end="\n\n")
	elif num == int(menuChk[1]) :
		print("추가 등록", end="\n\n")
	elif num == int(menuChk[2]) :
		print("학생 목록", end="\n\n")
		for i in range(len(menuList)):
			print(menuList[i], end="\t")
		print()
		print("-"*70)
		for i in range(len(idList)) :
			print(idList[i], end="\t")
			for j in range(len(scoreList[i])):
				print(scoreList[i][j], end="\t")
			print()
		print("-"*70)
	elif num == int(menuChk[3]) :
		print("합격생 목록", end="\n\n")
	else :
		print("번호를 확인하세요", end="\n\n")
	