#Python03_22_Chap03Practice_03_신동혁
for a in range(1,6) :
	for b in range(0,a) :
		print("*", end="")
	print()

print("\n")

c=1
while c<6 :
	print("*"*c)
	c = c + 1

print("\n")

d=0
while True :
	d += 1
	if d>5 : break
	print("*"*d)