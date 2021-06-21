#Python06_09_DictionaryEx06_신동혁
# Key로 Value 얻기 ==> get()
a = {"Name" : "SDH", "Phone" : "01077074510", "Birth" : "1224"}
print(a.get("Name"))
print("-"*20)
'''
get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
a["nokey"]는 Key 오류를 발생시키고 a.get("nokey")는 None을 돌려준다는 차이가 있다.
'''
print(a.get("nokey"))
#print(a.["nokey"])
print("-"*20)