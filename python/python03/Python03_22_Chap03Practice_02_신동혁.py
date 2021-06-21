#Python03_22_Chap03Practice_02_신동혁
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
a=0
i=1
while i <= 1000 :
	if i % 3 == 0 :
		a = a + i
	i = i + 1
print(a)

print()

b=0
for j in range(1,1001) :
	if j % 3 == 0 :
		b = b + j
print(b)