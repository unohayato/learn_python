import numbers
from pprint import pformat
from unittest import result


func = lambda x, y: print(f'{x}さんは{y}です。')

func('鈴木', '学生')


n1 = ['鈴木', '田中', '佐藤']
n2 = ['太郎', '二郎', '三郎']
result = list(map(lambda x, y: x + y + 'さん', n1 ,n2))
print(result)


numbers = [2, 4, 6, 8, 10, 12]

result2 = list(filter(lambda x: x >= 10, numbers))
print(result2)