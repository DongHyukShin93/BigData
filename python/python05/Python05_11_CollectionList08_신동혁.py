#Python05_11_CollectionList08_신동혁
#리스트 요소 제거(remove)_첫 번째 3만 제거
a=[1,2,3,2,3 ]
result01=a.remove(3)
print(result01)
print(a)

print('-'*20)
'''
우리 보통 파일형식처럼 붙여넣기를 계속 한다기 보다는 특정 리스트에서 그 값을 가져오고
대상 리스트에서는 그 값을 지우고 싶을 때 사용해요!
보통은 그 값을 index로 찾아서 그 값을 다른 변수에 넣고 다시 리스트에서 삭제하는 식으로 3번의 작업을 해야 하는데
그걸 한 번으로 줄여줬어요
'''
a=[1,2,3]
result02=a.pop(0)
print(result02)
print(a)

print('-'*20)
