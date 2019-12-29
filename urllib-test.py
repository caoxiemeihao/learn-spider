from urllib import request

# urlopen
resp = request.urlopen('https://www.baidu.com')
data = resp.read(10)  # 读取全部 10 大小
data = resp.readline()  # 读取一行
data = resp.readlines()  # 读成列表
code = resp.getcode()  # 响应状态码

print(data)
print(code)

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
