#Pandas02_16_ModuleEx02_신동혁
# from을 사용하면 mod1.sum(a,b)에서 "mod1." 이 부분을 생략할 수 있다.
from mod1 import sum, safe_sum
print(sum([1,3],[2,4]))
print(safe_sum(7,8))