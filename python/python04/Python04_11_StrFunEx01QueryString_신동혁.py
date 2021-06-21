#Python04_11_StrFunEx01QueryString_신동혁
a="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python"
'''
b=a.replace('https://search.naver.com/search.naver','URL')
c=b.replace('?','\n')
d=c.replace('&','\n')
print(d)
'''

www=a.split('?') #['https://search.naver.com/search.naver', 'where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=python']
urlList=www[1].split('&') #len(www) == 2

for i in range(len(www)) : # 0, 1 (두 번 돈다)
	if i == 0 :
		www[i] = "URL"
		print(www[i])
	elif i == 1 :
		www[i] = "Query"
		print(www[i])
for j in range(len(urlList)) :
	print("%s"%(urlList[j])) # 앞 쪽에 들여쓰기 방법 묻기
print("Query의 갯수는 %d개입니다"%len(urlList))
'''
for i in range(len(www)) :
	print(www.replace(www[0],"URL")
	print(www.replace(www[1],"Query")
'''