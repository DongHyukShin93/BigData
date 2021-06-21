#Pandas02_06_lambdaEx02_신동혁
# lambda 활용법
x = lambda a : a + 10
print(x(5)) # a = 5 -> 5 + 10

x = lambda a, b : a*b
print(x(4,5)) # a = 4, b = 5 -> 4*5

def myfunc(n) :
	return lambda a : a*n

mydoubler = myfunc(2) # mydoubler = lambda a : a*n(=2)
print(mydoubler(11)) # a = 11, n = 2 -> 11*2

mytripler = myfunc(3)
print(mytripler(11)) # a = 11, n = 3 -> 11*3