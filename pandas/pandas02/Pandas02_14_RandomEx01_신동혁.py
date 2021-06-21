#Pandas02_14_RandomEx01_신동혁
print("랜덤으로 숫자 뽑기\n")

import random

print("-"*25)

for i in  range(5) :
	print("%0.3f" % random.random(), end=" ") # random의 Defualt값은 0~1이다.
print()
print("-"*25)

for i in  range(5) :
	print("%d" % random.randint(1,3), end=" ")
print()
print("-"*25)

for i in  range(6) :
	print("%d" % random.randint(1,45), end=" ")
print()