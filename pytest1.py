import math
import pytest


def root(a,b):
    try:
        result = math.sqrt(a/b)
        print(result)
    except(ZeroDivisionError):
        result = 'Деление на ноль'
        print('Деление на ноль')
    except(TypeError):
        result = 'Ошибка типов данных'
        print('Ошибка типов данных')
    except(ValueError):
       result = 'Извлечение корня из отрицательного числа'
       print('Извлечение корня из отрицательного числа')
    except Exception as e:
        result = 'Тип ошибки: {e}'
        print(f'Тип ошибки: {e}') 
    return result

def test_two_pos():
    assert root(1,3) == 0.5773502691896257

def test_zero():
    assert root (1,0) == 'Деление на ноль'

def test_one_neg():
    assert root(1,-1) == 'Извлечение корня из отрицательного числа'

# python -m pytest D:\glal64\testing\pytest1.py