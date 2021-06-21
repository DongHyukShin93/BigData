#Python06_22_DataTypeEx07_신동혁
#다른 주소를 가리키도록 만들 수는 없을까?
a = [1,2,3]
b = a[:]
a[1] = 4
print(a, "\t", b)

from copy import copy # import는 내부에 빌트되어 있지 않은 함수 or 명령어를 가져온다
a = [1,2,3]
b = copy(a)
print(b)
print(id(a)) # 3036778696264
print(id(b)) # 3036776444104