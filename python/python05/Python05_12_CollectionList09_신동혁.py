#Python05_12_CollectionList09_신동혁
#리스트에 포함된 요소 x의 갯수 세기(count)
a=[1,2,3,1]
print(a.count(1))
print('-'*20)
'''
리스트 확장(extend)
extend(x) 에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에서 x리스트를 더한다.
'''
a=[1,2,3]
a.extend([4,5])
print(a)
# a.extend([4,5]) 는 a += [4,5]