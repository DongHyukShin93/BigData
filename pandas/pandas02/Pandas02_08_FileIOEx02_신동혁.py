#Pandas02_08_FileIOEx02_신동혁
'''
1. readline() 함수 이용하기
	- 첫 번째 줄 읽어 출력
2. readlines 함수 사용하기
	- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
	- 파일의 내용 전체를 문자열로 돌려준다.
'''
# 1. readline() 함수 이용하기
f1 = open("새파일.txt", "r")
line = f1.readline()
print(line)
f1.close()

print("-"*20)

#만약 모든 줄을 읽어서 화면에 출력하고 싶다면 다음과 같이 작성하면 된다.
f2 = open("새파일.txt", "r")
while True :
	line = f2.readline()
	if not line : break # line의 문장이 없으면(True) while문을 break하라.
	print(line)
f2.close()