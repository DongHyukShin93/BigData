#Python06_07_DictionaryEx04_신동혁
'''
딕셔너리 관련 함수들
Key 리스트 만들기 ==> keys()
'''
a = {"Name" : "SDH", "Phone" : "01077074510", "Birth" : "1224"}
print(a.keys())
'''
dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도
기본적인 반복(iterate) 구문 (예 : for문)을 이용할 수 있다.
'''
for k in a.keys() :
	print(k)
print("-"*20)
# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList = list(a.keys())
print(vList)
print("-"*20)