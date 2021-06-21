menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0

for i in range(len(idList)):
	dic[idList[i]] = scoreList[i]

print('-'*80)
print("학생관리시스템v01")
print('-'*80)
for i in range(len(menu)):
	print(menu[i], end='\t')
print()
print('-'*80)

while True:
	menuBtn = input('\t\t메뉴의 번호를 선택하세요. : ')
	if menuBtn == '':							# 엔터 오류 방지
		print("\t공백 입력..! 다시 입력하세요.")
		continue
	if menuBtn in menuChk:
		if menuBtn == '9':						# 9번은 int하지 않았기에 문자 비교
			print("\t종료합니다.")
			print(end='\t')
			break
		menuBtn = int(menuBtn)					# 이 줄에서 int 캐스팅
		print("\t%s" %menu[menuBtn-1])
		if menuBtn == 1:
			pass
		elif menuBtn == 2:
			pass
		elif menuBtn == 3:
			for k in range(len(MenuList)):		# MenuList < ID	필기	실기	인성	합계	평균	합격유무 >
				print(MenuList[k],end='\t')
			print()
			print('-'*60)
			for k in dic.keys():
				print(f"{k}\t{dic[k][0]}\t{dic[k][1]}\t{dic[k][2]}\t{sum(dic[k])}\t{sum(dic[k])/3:<.2f}",end='\t')
				#	[47, 58, 85]
				print("합격" if sum(dic[k]) >= 180 else "불합격")
			print('-'*60)
	else:
		print("\t다시 입력하세요.")
