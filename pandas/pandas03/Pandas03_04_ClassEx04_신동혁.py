#Pandas03_04_ClassEx04_신동혁
'''
- 하나의 클래스 안에 같은 메서드(==함수)가 있는 것을 Overload 라고 한다. cf) Override - 상속의 개념
- 어떻게 구분하나? 함수명()일 때, ()안의 매개변수의 갯수로 구분한다.
- 생성자(Constructor) : 함수, 클래스이름과 동일한 함수, 주로 초기화할 때 사용
'''
class FourCal :
	def __init__(self) :
		pass
	def __init__(self, first, second) : # __init__() - 생성자(Constructor) : 함수, 클래스이름과 동일한 함수, 
		self.first = first                        #                                                    주로 초기화할 때 사용
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

a = FourCal()


a = FourCal(6,3) # __init__() - 생성자(Constructor) : 함수, 클래스이름과 동일한 함수, 주로 초기화할 때 사용
# a.__init__(6,3) # 틀림
print("%d＋%d = %d" %(a.first, a.second ,a.sum()))
print("%d－%d = %d" %(a.first, a.second ,a.sub()))
print("%d×%d = %d" %(a.first, a.second, a.mul()))
print("%d÷%d = %d" %(a.first, a.second, a.div()))