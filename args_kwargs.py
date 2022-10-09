from cgitb import reset
import re
from unittest import result


def func(*args):
  result = ', '.join(args)
  print(result)

func('a')
func('a', 'b', 'c')

def func2(x, *args):
  result = ', '.join(args)
  print(f'{x}: {result}')
  
func2(1, 'a', 'b', 'c')

def func3(**kwargs):
  return kwargs

print(func3(name='田中', id=0, type='02'))