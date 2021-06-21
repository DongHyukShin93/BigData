#Python04_01_PrimeNumber_신동혁


while True :
	a=int(input(" >> 20이상의 정수를 입력하세요. [ Exit : 0 ] : "))
	b = 0
	if a >0 :
		for i in range(2,a) :
			b = 0
			for j in range(1,a+1) :
				if j%i == 0:
					b=1
				if b == 0 :
					c = "O."
				else :
					c = "X."
			print("%2d 소수 %s" %(j,c))
			'''
	elif 0 < a < 20 :
		print('"숫자를 확인하세요."')
	elif a == 0 :
		print("Exit")
		break

for i in range(2,a) :
	for j in range(i) :
		if  %  == 0 :
			b =  1
			c = "X."
		elif b == 0 :
			c= "O."
	print("%2d 소수 %s" %(j,c))
'''