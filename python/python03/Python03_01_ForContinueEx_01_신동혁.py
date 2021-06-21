#Python03_01_ForContinueEx_01_신동혁
grades = [90, 25, 67, 45, 80]
number = 0
for grade in grades :
	number = number + 1
	if grade < 60 :
		continue
	print(number,"번 학생 축하합니다! 합격입니다.")