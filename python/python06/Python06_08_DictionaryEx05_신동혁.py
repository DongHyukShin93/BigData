#Python06_08_DictionaryEx05_신동혁
#Value 리스트 만들기 ==> values()
a = {"Name" : "SDH", "Phone" : "01077074510", "Birth" : "1224"}
print(a.values())
print("-"*20)
#Key, Value 쌍 얻기 ==> items()
print(a.items())
print("-"*20)
# Key: Value 쌍 모두 지우기 ==> clear()
a.clear()
print(a)