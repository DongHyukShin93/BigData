#Python03_02_AddOddEven_신동혁

#1~10까지의 합
add = 0
for i in range(1,11) :
	add = add+i
print("1~10까지의 합",add)

#1~10까지의 홀수합
odd = 0
for i in range(1,11,2) :
	odd = odd + i
print("1~10까지의 홀수합",odd)

#1~10까지의 짝수합
even = 0
for i in range(2,11,2) :
	even = even + i
print("1~10까지의 짝수합",even)