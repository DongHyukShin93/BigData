#Pandas02_01_FunEx06_신동혁
# return문을 2번 사용하면,
# 두 번째 return문인 return a*b는 실행되지 않는다.
def add_and_mul(a, b) :
	return a+b
	return a*b # 두 번째 return문인 return a*b는 실행되지 않는다.
result = add_and_mul(3, 4)
print(result)
print("-"*20)

 # return의 또 다른 쓰임새
 # return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick) :
	if nick == "바보" :
		return
	print("나의 별명은 %s입니다." %nick)
say_nick("참새")
say_nick("바보")
print("-"*20)