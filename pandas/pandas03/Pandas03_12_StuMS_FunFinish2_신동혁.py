#Pandas03_10_StuMS_FunFinish_v02_신동혁
menu = ['1. 탈퇴학생 ', '2. 추가등록 ', '3. 학생목록 ', '4. 합격생목록 ','9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
menuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
passlist = [] # 지역변수 전역변수 헷갈림
newscore = []
idx = 0;

##########################  함수 모음 Start  ########################
# 1. 탈퇴 학생
def DelID() :
	delid = input("\n탈퇴할 학생의 ID를 입력하세요. (탈퇴하면 재가입할 수 없습니다.) ")
	if delid not in idList :
		print("\nID가 없습니다. 다시 입력하세요. ", end="\n\n")
	else :
		#idList.remove(delid) # 딕셔너리에서 삭제해줬기 때문에 idList에서 삭제해주지 않아도 된다.
		deleteIDList.append(delid)
		del dic[delid]
		print("\n'%s'학생이 탈퇴했습니다. 탈퇴 학생은 %d명입니다." %(delid, len(deleteIDList)), end="\n\n")

# 2. 추가 등록
def SignIn() :
	newscore = []
	while True :
		signid = input("\n등록할 ID를 입력하세요.  ")
		if signid in idList :
			print("\n이미 가입된 학생입니다. ", end="\n\n")
			continue
		elif signid in deleteIDList :
			print("\n탈퇴한 학생은 재가입할 수 없습니다.", end="\n\n")
			continue
		else :
			print("\n       ID : %s"%signid)
			# idList.append(signid) # dic이라는 딕셔너리에 바로 추가했기 때문에 따로 추가 ㄴㄴ
			for i in range(1,len(itemList)) :
				score = int(input(" %s : "%itemList[i]))
				newscore.append(score)
			dic[signid] = newscore
			# scoreList.append(newscore) # dic이라는 딕셔너리에 바로 추가했기 때문에 따로 추가 ㄴㄴ
			newscore = []
		print("\n추가등록이 완료되었습니다.", end = "\n\n")
		break

# idList = scoreList 딕셔너리
def InputData() :
    for i in range(len(idList)) :
        dic[idList[i]] = scoreList[i]

# 3. 학생목록
def PrintList() :
	print()
	for i in range(len(menuList)):
			print(menuList[i], end="\t")
	print()
	print("-"*70)
	for i in dic.keys() : #dic.keys()         #1 이중 for문 안 쓸 때
		print(i, end="\t")
		for j in range(len(scoreList[0])) : #1 f"{i}\t{dic[i][0]}\t{dic[i][1]}\t{dic[i][2]}\t{sum(dic[i])}\t{sum(dic[i])/3 : o.2f, end="\t"}"
			print(dic[i][j], end="\t")           #1 print("합격" if sum(dic[i]) >= 180 else "불합격")
		print(sum(dic[i]), end="\t") # sum(dic[i]) == dic[i][0] + dic[i][1] + dic[i][2]
		print("%0.2f" %(sum(dic[i])/len(dic[i])), end="\t")
		PorF = "합격" if sum(dic[i]) >= 210 else "불합격"
		print(PorF)
	print("-"*70)

# 4. 합격생 목록
def PassList() :
	#passlist = [] # 지역변수 전역변수 헷갈림
	print()
	for i in dic.keys() :
		if i in passlist :
			pass
		elif sum(dic[i]) >= 210 :
			passlist.append(i)
	print("합격생 : ", end="")
	for j in passlist :
		print(j, end="  ")
	print("\n합격생은 %d명입니다."%len(passlist),end="\n\n")

def MainPg() :	
	num = input("메뉴 번호 입력 : ")
	if num == "" :
		print("\n번호를 확인하세요", end="\n\n")
	elif num == menuChk[0] :
		DelID()
	elif num == menuChk[1] :
		SignIn()
	elif num == menuChk[2] :
		PrintList()
	elif num == menuChk[3] :
		PassList()
	elif num == menuChk[4] :
		print("\n학생 관리 시스템을 종료합니다.", end="\n\n")
		exit()
	else :
		print("\n번호를 확인하세요", end="\n\n")
###########################  함수 모음 End  ########### 
##########   Program Start  ####################
print("-"*80)
print("{0:^70}".format(" 학생 관리 시스템"))
print("-"*80)
for i in range(len(menu)) :
	print("%s" %menu[i], end="\t")
print()
print("-"*80)

InputData()
while True :
	MainPg()