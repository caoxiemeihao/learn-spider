from urllib import parse


def _urlencode():
    params = {'name': 'Andy', 'age': 33, 'job': 'BOSS zhou'}
    result = parse.urlencode(params)
    print(result)
    result2 = parse.parse_qs(result)
    print(result2)


def _urlparse():
    url = 'https://www.baidu.com/baidu?&ie=utf-8&word=node.js'
    # result = parse.urlparse(url)
    # 'https://www.baidu.com/baidu;params?&ie=utf-8&word=node.js'
    result = parse.urlsplit(url)  # 比 urlparse 少了一个 params
    print(result)


if __name__ == '__main__':
    _urlencode()
    ...
    _urlparse()
