#Python05_13_EmployeeStep01_신동혁
#인사 관리 시스템
#t : 계약직 , r : 정규직
#구분 == 사번
TName = ["구분","사원명","입사일","급여"]

empInfo = [
['T160501',"캔디","2016-05-10"],
['R160510',"장미","2016-05-10"],
['t160811',"튤립","2016-08-15"],
['T160821',"포도","2016-08-22"],
['r160850',"사과","2016-08-30"]
]
empPayTable = [[250,10], [200,12], [300,9], [230,11], [150,12]]

for i in range(len(TName)) :
	print(TName[i], end='    ')
print()
print('-'*40)
for i in range(5) : # 5 X ==> len()
	empNum=empInfo[i][0][0]
	if empNum =='T' or empNum == 't' :
		print('계약직',end='\t')
	elif empNum =='R' or empNum == 'r' :
		print('정규직',end='\t')	
	for j in range(1,3) :
		print(empInfo[i][j],end='\t')
	for k in range(1) :
		print("%d만원"%(empPayTable[i][0]*empPayTable[i][1]), end=" ")
	print()
'''
empPayTable[i][0]*empPayTable[i][1]
'''