from urllib import parse


def _urlencode():
    params = {'name': 'Andy', 'age': 33, 'job': 'BOSS zhou'}
    result = parse.urlencode(params)
    print(result)
    result2 = parse.parse_qs(result)
    print(result2)


if __name__ == '__main__':
    _urlencode()
