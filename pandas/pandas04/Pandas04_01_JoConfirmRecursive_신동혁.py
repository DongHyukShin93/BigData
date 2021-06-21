import random
lst = []

def recursive(m) :    # 첫 번째 m == 입력한 인원수
	if chk == len(lst) : # 인원수와 랜덤 숫자의 갯수가 같을 때
		return               # 재귀함수
	
	for i in range(m) :
		num = random.randint(1,len(name))
		if num not in lst :
			lst.append(num)
		else :
			recursive(chk - len(lst)) # 여기서 m이 변한다. name에 저장된 갯수에서 lst에 저장된 갯수를 뺀다.

while True :
	name = input("4인 이상의 이름을 입력하세요. ").split()
	if len(name) < 4 :
		print("\n인원수가 부족합니다. 다시 입력하세요.", end="\n\n")
	elif len(name) >= 4 :
		for i in name :
			print(i, end="\t")
		print()

		chk = len(name)

		lst = []
		recursive(chk)

		for j in lst :
			print(j, end="\t")
		print()