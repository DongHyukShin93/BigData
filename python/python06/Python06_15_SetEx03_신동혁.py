#Python06_15_SetEx03_신동혁
#집합 자료형 관련 함수들
# 값 1개 추가하기(add)
s1 = set([1,2,3,])
s1.add(4)
print(s1)
# 값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
# 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
print(s1)