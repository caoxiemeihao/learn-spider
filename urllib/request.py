# Python
# int float bool
# 1 2 3
# 1.2
# True False

# list tuple set
# ['a', False, 2]
# ('a', True, 123)
# {'a', 2}

# dict
# {'a': 1, 'b': 2}

from urllib import request


# urlopen
def _urlopen():
    resp = request.urlopen('https://www.baidu.com')
    data = resp.read(10)  # 读取全部 10 大小
    line = resp.readline()  # 读取一行
    lines = resp.readlines()  # 读成列表
    code = resp.getcode()  # 响应状态码


# urlretrieve
def _urlretrieve():
    request.urlretrieve('https://p0.ssl.qhimg.com/t01e7dd4751265462d1.gif', '../raw/test.gif')


if __name__ == '__main__':
    _urlopen()
    _urlretrieve()
