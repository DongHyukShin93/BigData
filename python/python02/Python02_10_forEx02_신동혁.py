#Python02_10_forEx02_신동혁
marks = [90, 25, 67, 45, 80]
number=0
for mark in marks :
	number=number+1 # number += 1
	if mark>=60 :
		print(number,"번 학생은 합격입니다.")
	else :
		print(number,"번 학생은 불합격입니다.")