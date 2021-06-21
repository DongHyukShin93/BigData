#Pandas03_05_ClassEx05_신동혁
'''
# 생성자 ( Constructor )
# 상속 : 일반화
** 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에
     상속할 클래스 이름을 넣어주면 된다.
형식] class 새로운 클래스 이름(상속할 클래스 이름)
'''
class FourCal :
	def __init__(self) :
		pass
	def __init__(self, first, second) :
		self.first = first
		self.second = second
	
	def sum(self) :
		result = self.first + self.second
		return result

	def sub(self) :
		result = self.first - self.second
		return result

	def mul(self) :
		result = self.first * self.second
		return result

	def div(self) :
		result = self.first / self.second
		return result
	
class MoreFourCal(FourCal) : # 형식] class 새로운 클래스 이름(상속할 클래스 이름)
	def pow(self, su01) :
		result = su01**2
		return result

a = MoreFourCal(4,2)
b = a.pow(5)
print("%d＋%d = %d" %(a.first, a.second ,a.sum()))
print("%d－%d = %d" %(a.first, a.second ,a.sub()))
print("%d×%d = %d" %(a.first, a.second, a.mul()))
print("%d÷%d = %0.1f" %(a.first, a.second, a.div()))
print("제곱출력 : %d" %(b))