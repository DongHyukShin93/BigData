#Pandas03_03_ClassEx03_신동혁
class FourCal() :
	def  setdata(self, first, second) :
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

a = FourCal()
a.setdata(6,3)
print("%d＋%d = %d" %(a.first, a.second ,a.sum()))
print("%d－%d = %d" %(a.first, a.second ,a.sub()))
print("%d×%d = %d" %(a.first, a.second, a.mul()))
print("%d÷%d = %d" %(a.first, a.second, a.div()))