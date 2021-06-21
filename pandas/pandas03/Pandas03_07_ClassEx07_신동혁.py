#Pandas03_07_ClassEx07_신동혁
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

class SafeFourCal(FourCal) :
	def div(self) : # FourCal이라는 부모 클래스의 def div(self)이라는 메소드랑 똑같지만 현재 메소드를 우선으로 처리
		if self.second == 0 :                                                                           #를 if문으로 재정의 하고
			return 0
		else :
			return super().div() # super() 상위 클래스의 메소드로 처리, div(self)라고 쓰면 안됨
                                           # FourCal.div(self)
a = SafeFourCal(4,3)
print("%d＋%d = %d" %(a.first, a.second ,a.sum()))
print("%d－%d = %d" %(a.first, a.second ,a.sub()))
print("%d×%d = %d" %(a.first, a.second, a.mul()))
print("%d÷%d = %0.2f" %(a.first, a.second, a.div()))