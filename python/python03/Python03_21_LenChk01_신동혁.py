#Python03_21_LenChk01_신동혁
#평균 소수점 이하 2자리 확인
list01=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
print(len(list01))
sum = 0;
for score in list01 :
	sum = sum + score
print("합계 : %d" %sum)
print("평균 : %0.2f" %(sum/len(list01)))