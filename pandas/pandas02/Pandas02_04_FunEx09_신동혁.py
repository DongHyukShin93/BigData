#Pandas02_04_FunEx09_신동혁
# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 01. return 사용하기
a = 1
def vartest(a) :
	a += 1
	return a
a = vartest(a) # vartest(a)의 결괏값을 함수 밖의 변수(==전역 함수) a에 대입
print(a)
print("-"*20)

# 02. global 명령어 사용하기
# global 명령어 : 함수 안에서 함수 밖의 변수를 직접 사용할 때 사용. But 권장 X
# 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
a = 1
def vartest() :
	global a
	a += 1
vartest()
print(a)