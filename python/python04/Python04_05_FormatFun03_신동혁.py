#Python04_05_FormatFun03_신동혁
a="{2:<10}".format('aa','bb','cc')
b="{1:>10}".format('aa','bb','cc')
c="{0:^10}".format('aa','bb','cc')
d="{:w^10}".format('aa','bb','cc')
print(a)
print(b)
print(c)
print(d)

print()
x=342134234
y=3421.34236
e1="{1:0.4f}  {0:,d}".format(x,y)
e2='{:20.3f}'.format(y)
print(e1)
print(e2)