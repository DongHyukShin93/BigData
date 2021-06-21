#Python06_23_Chap02_신동혁
#Q01
print("Q 1. ", end="\n\n")
grade = [90, 75, 55]
result = 0
for i in range(len(grade)) :
	result += grade[i]
print("합계 : %d" %result)
print("평균 : %0.2f"%(result/len(grade)), end="\n\n")
#Q02
print("Q 2. ", end="\n\n")
num = int(input("정수를 입력하세요. "))
result01 = "홀수입니다." if num%2==1 else "짝수입니다."
print(result01, end="\n\n")
#Q03 & 04
print("Q 3 & 4. ", end="\n\n")
pin = "931224-3068234"
a = pin.split("-")
yyyymmdd = a[0]
num = a[1]
print(yyyymmdd)
print(num)
result02 = "남자입니다." if a[1][0] == 1 or num[0] == 3 else "여자입니다."
print(result02, end="\n\n")
#Q05
print("Q 5. ", end="\n\n")
a = "a:b:c:d"
b = a.replace(":","#")
print(b, end="\n\n")
#Q06
print("Q 6. ", end="\n\n")
a = [1,3,5,4,2]
a.sort()                                 # sort()는 오름차순 
a.reverse()                           # reverse()는 순서를 반대로
print(a, end="\n\n")
#Q07
print("Q 7. ", end="\n\n")
a = ["Life","is","too","short"]
result = " ".join(a)                     # " "이런 공백도 join()을 이용할 수 있다.
print(result, end="\n\n")
#Q08
print("Q 8. ", end="\n\n")
a = (1,2,3)
b = a + (4,)                             # a = a + (4,)라고 써도 된다. 굳이 변수 b를 사용하지 않아도 된다.
print(b, end="\n\n")
#Q09
print("Q 9. ", end="\n\n")
a = dict()
a["name"] = "python"
a[("a",)] = "python"
# a[[1]] = "python"               # 딕셔너리의 Key값은 변하면 안되는데,
                                            #  a[[1]]에서 딕셔너리 a의 Key값이 변경이 가능한 리스트형=[1]이기 때문에 오류가 발생한다.   
a[250] = "python"
print(a, end="\n\n")
#Q10
print("Q 10.", end="\n\n")
a = {"A" : 90, "B" : 80, "C" : 70}
result = a.pop("B")                  #딕셔너리에도 pop 함수를 사용할 수 있다.
print(a)
print(result, end="\n\n")