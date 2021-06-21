answer=[]
fruitCnt=[]
while True :
	num = int(input(" 10 이상의 정수를 입력하세요. [ Exit : 0] "))
	if num == 0 :
		print(" 종료합니다. ")
		break
	if num >= 10 :
		for i in range(1,num+1) :
			if i%3==0 :
				answer.append('Apple')
			if i%4==0 :
				answer.append('Melon')
			if i%5==0 :
				answer.append('Grape')
			if i%8==0 :
				answer.append('StrawBerry')
			fruitCnt += answer
			if len(answer)==0 :
				print('%d. '%i)
			else :
				print('%d. '%i, answer)
		print('==<< Fruit List Count >>==')