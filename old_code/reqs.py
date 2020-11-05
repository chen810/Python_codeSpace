import requests


def sta(x):
    print(type(x.status_code), x.status_code)
    print(type(x.headers), x.headers)
    print(type(x.cookies), x.cookies)
    print(type(x.url), x.url)
    print(type(x.history), x.history)
    print('==========================================================================================================')
def pp():
    print("test")
    return 0

url = 'https://www.12306.cn/index/'

header = {
    # 构造请求头
}
"""
file = {'file': open('filename', 'mod')}
可利用此语句上传文件。令参数files=files
"""
if __name__ == '__main__':
    r = requests.get(url, headers=header)
    print(r.text)
    print(r.content)
    sta(r)

