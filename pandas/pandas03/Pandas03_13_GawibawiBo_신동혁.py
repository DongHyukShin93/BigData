#Pandas03_13_GawibawiBo_신동혁
import sys
import random
menuList = ["가위", "바위", "보", "횟수 입력", "종료"]
menuChk = [1, 2, 3, 4, 9]
comwin = 0
userwin = 0
total = 0

#################  함수 목록 Start  #################
# Uesr Interface
def UI() :
	print("{0:=^38}".format("Com vs Human 가위바위보 게임"))
	print("-"*46)
	print()
	for i in range(len(menuChk)) :
		print("%d. %s " %(menuChk[i],menuList[i]), end=" ")
	print("\n")
	print("-"*46, end="\n\n")
'''
# RockScissorsPaper dic
def rspDic() :
	rspDic = {}
	for i in range(3) :
		rspDic[menuChk[i]] = menuList[i]

# RockScissorsPaper

def userScissors():
	print("Com : %s / User : %s ", end="\t")  # rspDic[comNum], rspDic[userNum]을 포매팅할 수 없음
	if comNum == 2 : # 여기서 comNum을 인식하지 못함
		print("Com Win ! 컴퓨터가 이겼습니다 !")
		comwin += 1
	elif comNum == 3 :
		print("You Win ! 당신이 이겼습니다 !")
		userwin += 1
	elif comNum == int(userNum) :
		print("Draw ! 무승부입니다 ! ")
	print("\n=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다." %(comwin, userwin), end="\n\n")
	total += 1

# Draw
def draw(userNum) : # dram 함수의 입력값에 userNum을 넣어줬다.
	if comNum == int(userNum) : # userNum를 인식하지 못함
		print("Draw ! 무승부입니다 ! ")
'''
# MainProGram
def MainPG() :
	UI()
	userNum = input("\t번호를 선택하세요. ")
	global comwin # global은 잘 안쓰는게 좋다. 
	global userwin
	global total
	comNum = random.randint(1,3)
	if userNum == "" :
		print("\n 잘못입력했습니다. 다시 입력하세요. ", end="\n\n")
	elif comNum == int(userNum) :
		print(f"Com : {menuList[comNum-1]} / User : {menuList[int(userNum)-1]}\tDraw ! 무승부입니다 ! ")
		print("\n=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다." %(comwin, userwin), end="\n\n")
		total += 1
	elif int(userNum) == menuChk[0]:
		if comNum == 2 :
			print(f"Com : {menuList[1]} / User : {menuList[0]}\tCom Win ! 컴퓨터가 이겼습니다 !")
			comwin += 1
		elif comNum == 3 :
			print(f"Com : {menuList[2]} / User : {menuList[0]}\tUser Win ! 당신이 이겼습니다 !")
			userwin += 1
		print("\n=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다." %(comwin, userwin), end="\n\n")
		total += 1
	elif int(userNum) == menuChk[1]:
		if comNum == 3 :
			print(f"Com : {menuList[2]} / User : {menuList[1]}\tCom Win ! 컴퓨터가 이겼습니다 !")
			comwin += 1
		elif comNum == 1 :
			print(f"Com : {menuList[0]} / User : {menuList[1]}\tYou Win ! 당신이 이겼습니다 !")
			userwin += 1
		print("\n=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다." %(comwin, userwin), end="\n\n")
		total += 1
	elif int(userNum) == menuChk[2]:
		if comNum == 1 :
			print(f"Com : {menuList[0]} / User : {menuList[2]}\tCom Win ! 컴퓨터가 이겼습니다 !")
			comwin += 1
		elif comNum == 2 :
			print(f"Com : {menuList[1]} / User : {menuList[2]}\tUser Win ! 당신이 이겼습니다 !")
			userwin += 1
		print("\n=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다." %(comwin, userwin), end="\n\n")
		total += 1
	elif int(userNum) == menuChk[3]: # 고치기
		print("\n\t총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다." %(total, comwin, userwin), end="\n\n")
	elif int(userNum) == menuChk[4]:
		print("\n\t총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다." %(total, comwin, userwin), end="\n\n")
		if comwin > userwin :
			print(" 따라서 최종 스코어 %d : %d (컴퓨터 : 당신)(으)로 컴퓨터의 승리입니다." %(comwin, userwin), end="\n\n")
		elif comwin < userwin :
			print(" 따라서 최종 스코어 %d : %d (컴퓨터 : 당신)(으)로 당신의 승리입니다." %(comwin, userwin), end="\n\n")
		else :
			print(" 따라서 최종 스코어 %d : %d (컴퓨터 : 당신)(으)로 무승부입니다." %(comwin, userwin), end="\n\n")
		exit()
	else :
		print("\n 잘못입력했습니다. 다시 입력하세요. ", end="\n\n")
#################  함수 목록 End  #################
while True :
	MainPG()