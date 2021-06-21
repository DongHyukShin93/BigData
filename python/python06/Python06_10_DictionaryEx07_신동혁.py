#Python06_10_DictionaryEx07_신동혁
'''
딕셔너리 안에 찾으려는 Key 값이 없을 경우 
미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리하다.
a 딕셔너리에는 'foo'에 해당하는 값이 없다. 따라서 디폴트 값인 'bar'를 돌려준다.
'''
a = {"Name" : "SDH", "Phone" : "01077074510", "Birth" : "1224"}
print(a.get("z","y"))
print("-"*20)

# 해당 Key가 딕셔너리 안에 있는지 조사하기 ==> in
a = {"Name" : "SDH", "Phone" : "01077074510", "Birth" : "1224"}
print("Name" in a)
print("Email" in a)