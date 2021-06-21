#Python03_13_StarEx02_2_신동혁
a = int(input("열 갯수를 입력해 주세요 : "))
for i in range(a,0,-1) :   #range(a,b,여기 음수가 들어가면 반대로 이동 -> ex : -1)
	for j in range(i) :
		print('*',end="")
	print()