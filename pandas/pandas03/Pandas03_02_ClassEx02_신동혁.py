#Pandas03_02_ClassEx02_신동혁
'''
[메서드의 또 다른 호출 방법]
	- 클래스를 통해 메소드를 호출하는 것도 가능                                    함수 :
	- 클래스 이름.메소드 형태로 호출할 때는 객체 a를 첫 번째                         - 재사용
	  매개변수 self에 꼭 전달해주어야 한다.                                                    - 함수명()
	- 반면에 다음처럼 객체.메서드 형태로 호출할 때는                             함수가 클래스안으로 가면 메소드라고 한다.
	   self를 반드시 생략해서 호출해야 한다.
'''
class FourCal :
	def setdata(self, first, second) :
		self.first = first
		self.second = second

a = FourCal()

FourCal.setdata(a, 2, 3) # 클래스 이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해주어야 한다.

print(a.first, a.second)
a.setdata(4, 5) # 반면에 다음처럼 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.
print(a.first, a.second)