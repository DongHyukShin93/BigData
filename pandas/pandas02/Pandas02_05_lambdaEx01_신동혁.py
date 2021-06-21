#Pandas02_05_lambdaEx01_신동혁
'''
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 
보통 함수를 한줄로 간결하게 만들 때 사용한다. 
우리말로는 "람다"라고 읽고 
def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

사용형식
< 함수명 = lambda 매개변수1, 매개변수2,... : 매개변수를 이용한 표현식 >
'''
add = lambda a, b : a + b # == def add(a, b) :
result = add(8,7)            #		   return a + b
print(result)

# lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

print("-"*20)

def add(a,b) :
	return a+b
print(add(7,5))