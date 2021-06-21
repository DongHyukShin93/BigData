#Python06_11_StudentMS_Step01_v01_신동혁
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
	for i in range(len(menu)) :
		if num == int(menuChk[i]) :
			print(menu[i], end="\n\n")
	if num == 9 :
			print("학생 관리 시스템을 종료합니다.", end="\n\n") # end = "\n" 이용합시다
			break
	elif num <= 0 or num >=5:
		print("번호를 확인 하세요.", end="\n\n")
	'''
	if num == int(menuChk[4]) :
		print("학생 관리 시스템을 종료합니다.")
		print()
		break
	elif num == int(menuChk[0]) :
		print("탈퇴 학생")
		print()
	elif num == int(menuChk[1]) :
		print("추가 등록")
		print()
	elif num == int(menuChk[2]) :
		print("학생 목록")
		print()
	elif num == int(menuChk[3]) :
		print("합격생 목록")
		print()
	else :
		print("번호를 확인하세요")
		print()
'''