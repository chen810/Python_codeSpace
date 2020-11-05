a=input('输入汉字：')
a=a.encode('utf-8')
a=str(a)
a=a[2:-1]
a=a.split('\\x')
a='%'.join(a)
for i in a:
    a=a.upper()

print(a)
