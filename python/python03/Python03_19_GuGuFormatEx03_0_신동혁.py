#Python03_19_GuGuFormatEx03_신동혁
for a in range(2,10) :
	print("# %d 단"%a , end="    ")
print("\n")
print("="*80)
for i in range(2,10) :
	for j in range(2,10) :
		print("%d×%d=%3d"%(j,i,j*i) ,end="  ")
	print()
print('\n')

'''
# 내가 틀린거
c=0
while c < 10 :
	while d == c :
		print("%d×%d=%3d" % (d,c,d*c) , end="  ")
		d += 1
	c += 1
	print()

c=2
while c < 10:
	d=2
	while d < 10:
		print("%d×%d=%3d" % (d,c,d*c) , end="  ")
		d+=1
	c+=1
	print()
'''

c=2
while c < 10 :
	d=2
	if d <10 : # if ==> while
		print("%d×%d=%3d"%(d,c,c*d) , end="  ")
		d+=1
	c+=1
	print()