#Pandas03_01_ClassEx01_신동혁
# read_csv(filepath_or_buffer[, sep, …]) []안의 요소는 생략가능
# Read a comma-separated values (csv) file into DataFrame.
'''
** 클래스란
클래스 - 틀이자 구조이다 (예 : 클래스가 프랜차이즈 본사라면, 객체는 프랜차이즈 지점이다.)
           - 함수 + 속성(은 변수라고 생각하면 편함)
    -> 객체 : 클래스로부터 생성
생성자 : 함수로써 클래스이름과 동일한 함수이다, 주로 초기화할 때 사용
** 클래스를 어떻게 사용할까
클래스 사용
    - 객체 생성 후 사용
	- 형식 : 객체.속성 or 객체.함수
self는 현재 객체를 의미 (Java에서는 this를 사용함)
'''
class FourCal :
	def setdata(self, first, second) : # self는 매개변수 X
		self.first = first
		self.second = second

a = FourCal()       # 클래스 FourCal가 a에 연결 됐다 == a라는 객체를 생성 후 사용
a.setdata(4,8)

print(a.first)
print(a.second)
print(type(a)) # < class '__main__.FourCal'>