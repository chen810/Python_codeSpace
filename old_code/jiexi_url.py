from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin


def you(x):
    if not x:
        print('None!!!', end='')


def tog(x):
    cc = []
    for k in x:
        cc.append(k)
    return cc


url = r"file://C:/Users/MISS/Desktop/1.txt"
url1 = 'https://www.baidu.com/s?wd=python'
result = urlparse(url)
result1 = urlparse(url1)
print(type(result), '\n', result)
for i in result:
    you(i)
    print(i)
print(type(result1), '\n', result1)
for j in result1:
    you(j)
    print(j)
sum0 = urlunparse(tog(result))
sum1 = urlunparse(tog(result1))
print(sum0)
print(sum1)
