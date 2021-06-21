#Pandas03_09_StudentMS_FunMunni_신동혁
menu = ['1. 탈퇴학생 ', '2. 추가등록 ', '3. 학생목록 ', '4. 합격생목록 ','9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
menuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
#########  함수 모음 Start  #########
# 1. 탈퇴 학생
def DelID() :
	print()
	print("탈퇴 학생", end="\n\n")
# 2. 추가 등록
def SignIn() :
	print()
	print("추가 등록", end="\n\n")
# 4. 합격생 목록
def PassList() :
	print()
	print("합격생 목록", end="\n\n")
# 3. 학생목록
def PrintList() :
	for i in range(len(menuList)):
			print(menuList[i], end="\t")
	print()
	print("-"*70)
	for i in dic.keys() : #dic.keys()  #1 이중 for문 안 쓸 때
		print(i, end="\t")
		for j in range(len(scoreList[0])) : #1 f"{i}\t{dic[i][0]}\t{dic[i][1]}\t{dic[i][2]}\t{sum(dic[i])}\t{sum(dic[i])/3 : o.2f, end="\t"}"
			print(dic[i][j], end="\t")           #1 print("합격" if sum(dic[i]) >= 180 else "불합격")
		print(sum(dic[i]), end="\t")
		print("%0.2f" %(sum(dic[i])/len(scoreList[0])), end="\t")
		PorF = "합격" if sum(dic[i]) >= 210 else "불합격"
		print(PorF)
		print()
	print("-"*70)
# idList = scoreList 딕셔너리
def InputData() :
    for i in range(len(idList)) :
        dic[idList[i]] = scoreList[i]
    return dic

def MainPg() :

	num = input("번호 입력 : ")
	if num == "" :
		print()
		print("번호를 확인하세요", end="\n\n")
	elif num == menuChk[0] :
		DelID()
	elif num == menuChk[1] :
		SignIn()
	elif num == menuChk[2] :
		PrintList()
	elif num == menuChk[3] :
		PassList()
	elif num == menuChk[4] :
		print()
		print("학생 관리 시스템을 종료합니다.", end="\n\n")
		exit()
	else :
		print()
		print("번호를 확인하세요", end="\n\n")
################ ############## 함수 모음 End  ########### 
##########   Program Start  ##########
print("-"*80)
print("{0:^68}".format("학생 관리 시스템v01"))
print("-"*80)
for i in range(len(menu)) :
	print("%s" %menu[i], end="\t")
print()
print("-"*80)

InputData() # idList = scoreList 딕셔너리
while True :
	MainPg()