import time
import sys
import os
import re
import random
black, red, green, yellow, blue, purple, cyan, white = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
b_black, b_red, b_green, b_yellow, b_blue, b_purple, b_cyan, b_white = '\033[90m', '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m'


bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_purple, bg_cyan, bg_white = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
bg_b_black, bg_b_red, bg_b_green, bg_b_yellow, bg_b_blue, bg_b_purple, bg_b_cyan, bg_b_white = '\033[100m', '\033[101m', '\033[102m', '\033[103m', '\033[104m', '\033[105m', '\033[106m', '\033[107m'


bold, italic, underline, strike = '\033[1m', '\033[3m', '\033[4m', '\033[9m'

 

def superprint(word, delay=0, color='', bg_color='', style='', end='\n'):
    prefix = ''
    if style:
        prefix += style
    if color:
        prefix += color
    if bg_color:
        prefix += bg_color
    
    # Если есть префикс, добавляем сброс в конце
    suffix = '\033[0m' if prefix else ''
    
    # Печатаем префикс (устанавливаем режим)
    if prefix:
        sys.stdout.write(prefix)
    
    # Печатаем слово по буквам
    for char in word:
        time.sleep(delay)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    # Сбрасываем режим (если был установлен)
    if suffix:
        sys.stdout.write(suffix)
    
    # Печатаем завершающий символ
    print(end=end, flush=True)



def loadspin(seconds, speed=10, color=''):
    import time
    import sys

    frames = ['|', '/', '-', '\\']
    start = time.perf_counter()
    i = 0

    # Если цвет задан — выводим его, потом анимацию, потом сбрасываем
    if color:
        sys.stdout.write(color)

    while time.perf_counter() - start < seconds:
        sys.stdout.write(f"\r{frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(1 / speed)
        i += 1

    # Сброс цвета и переход на новую строку
    if color:
        sys.stdout.write('\033[0m')
    print()


def smart_input(prompt, typ=str, delay=0, color=''):
    """
    Выводит приглашение с цветом и задержкой по буквам,
    затем запрашивает ввод и возвращает его с преобразованием типа.
    """
    # Устанавливаем цвет (если задан)
    if color:
        sys.stdout.write(color)
    
    # Выводим приглашение по буквам
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    # Сброс цвета перед вводом
    sys.stdout.write('\033[0m')
    
    # Запрашиваем ввод
    user_input = input()
    
    # Преобразуем тип
    try:
        return typ(user_input)
    except ValueError:
        return None
def bgcolor(color=None):
    """
    bgcolor(bg_blue) - установить фон
    bgcolor() - сбросить фон
    """
    if color:
        sys.stdout.write(f"{color}\033[2J\033[H\033[3J")
    else:
        sys.stdout.write("\033[0m\033[2J\033[H\033[3J")
    sys.stdout.flush()
    

def between(текст, word=None, left=None, right=None):
    if type(текст) is str:
        текст = текст.split()
    elif type(текст) is not list:
        return False
    try:
        позиция1 = текст.index(left)
        позиция2 = текст.index(word)
        позиция3 = текст.index(right)
        if позиция1 < позиция2 < позиция3 or позиция1 > позиция2 > позиция3:
            return True
    except Exception as e:
        return False
        
import math
import re

def calculate(expression):
    """
    Калькулятор с поддержкой:
    - Отрицательные числа (-2+3 = 1)
    - sin, cos (в градусах)
    - pi, e
    - log, log10, sqrt
    - ^, !, скобки
    """
    try:
        expression = expression.strip()
        
        # Константы
        expression = expression.replace('pi', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        # Замена символов
        expression = expression.replace('×', '*').replace('•', '*').replace('x', '*').replace('х', '*')
        expression = expression.replace('÷', '/').replace(':', '/')
        expression = expression.replace('^', '**')
        expression = expression.replace(' ', '')
        
        # Степени ², ³
        powers = {'²': '2', '³': '3', '⁴': '4', '⁵': '5'}
        for sym, num in powers.items():
            expression = expression.replace(sym, f'**{num}')
        
        # Факториал
        def factorial(n):
            if n < 0:
                return None
            if n == 0 or n == 1:
                return 1
            res = 1
            for i in range(2, int(n) + 1):
                res *= i
            return res
        
        # Функция для преобразования унарного минуса
        def fix_unary_minus(expr):
            """Превращает -2+3 в 0-2+3, (-5+3) в (0-5+3), *-5 в *0-5"""
            # Если выражение начинается с минуса
            if expr.startswith('-'):
                expr = '0' + expr
            # Минус после открывающей скобки
            expr = re.sub(r'\(-', '(0-', expr)
            # Минус после оператора
            expr = re.sub(r'([+\-*/])-', r'\1 0-', expr)
            # Убираем лишние пробелы
            expr = expr.replace(' ', '')
            return expr
        
        # Рекурсивный парсер
        def parse(expr):
            # Сначала преобразуем унарные минусы
            expr = fix_unary_minus(expr)
            
            # sin(30) в градусах
            expr = re.sub(r'sin\(([^()]+)\)', lambda m: str(math.sin(math.radians(float(parse(m.group(1)))))), expr)
            expr = re.sub(r'cos\(([^()]+)\)', lambda m: str(math.cos(math.radians(float(parse(m.group(1)))))), expr)
            
            # sqrt(16)
            expr = re.sub(r'sqrt\(([^()]+)\)', lambda m: str(math.sqrt(float(parse(m.group(1))))), expr)
            
            # log(100) - натуральный логарифм
            expr = re.sub(r'log\(([^()]+)\)', lambda m: str(math.log(float(parse(m.group(1))))), expr)
            
            # log10(100)
            expr = re.sub(r'log10\(([^()]+)\)', lambda m: str(math.log10(float(parse(m.group(1))))), expr)
            
            # Факториал 5!
            expr = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), expr)
            
            # Скобки
            while '(' in expr:
                expr = re.sub(r'\(([^()]+)\)', lambda m: str(parse(m.group(1))), expr)
            
            # Убираем двойные минусы и плюс-минусы (которые могли появиться)
            expr = expr.replace('--', '+')
            expr = expr.replace('+-', '-')
            expr = expr.replace('-+', '-')
            
            # Степень
            expr = re.sub(r'([\d.]+)\*\*([\d.]+)', lambda m: str(float(m.group(1)) ** float(m.group(2))), expr)
            
            # Умножение и деление
            while re.search(r'[\d.]+[*/][\d.]+', expr):
                expr = re.sub(r'([\d.]+)([*/])([\d.]+)',
                              lambda m: str(float(m.group(1)) * float(m.group(3)) if m.group(2) == '*' else float(m.group(1)) / float(m.group(3))),
                              expr)
            
            # Сложение и вычитание
            while re.search(r'[\d.]+[+\-][\d.]+', expr):
                expr = re.sub(r'([\d.]+)([+\-])([\d.]+)',
                              lambda m: str(float(m.group(1)) + float(m.group(3)) if m.group(2) == '+' else float(m.group(1)) - float(m.group(3))),
                              expr)
            
            return expr
        
        # Проверка, есть ли операторы
        if not any(op in expression for op in ["+", "-", "*", "/", "**", "sin", "cos", "sqrt", "log", "(", "!"]):
            return None
        
        result = parse(expression)
        res = float(result)
        
        if res.is_integer():
            return int(res)
        return round(res, 10)
    
    except Exception:
        return {}
        


def random_obj(список):
    return список[random.randint(0, len(список)-1)]    
        
def error(text):   superprint(text, color=red, style=bold)
def warn(text):    superprint(text, color=yellow, style=bold)
def success(text): superprint(text, color=green)
def info(text):    superprint(text, color=blue)
def levenshtein(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(
                prev[j] + 1,
                cur[-1] + 1,
                prev[j - 1] + (ca != cb)
            ))
        prev = cur
    return prev[-1]

def sim(слово1, слово2, порог=0.6):
    """Проверяет, похожи ли два слова (на основе расстояния Левенштейна)"""
    if not слово1 or not слово2:
        return False
    
    слово1 = слово1.lower()
    слово2 = слово2.lower()
    
    max_len = max(len(слово1), len(слово2))
    if max_len == 0:
        return True
    
    расстояние = levenshtein(слово1, слово2)
    коэффициент = 1 - (расстояние / max_len)
    return коэффициент >= порог
    
def formatcheck(слово, тип):
    return isinstance(слово, тип)
    
    



first = 0
last = -1
rand = "random"  # специальное значение

def order(список, порядок):
    if порядок == first:
        return список[first]
    elif порядок == last:
        return список[last]
    elif порядок == rand:
        return random.choice(список)

def timer(время, текст):
    time.sleep(время)
    print(текст)
    

def flatten(*списки):
    список = sum(списки, [])
    return список
    
def integers_between(low, high):
    """Возвращает список целых чисел от low до high включительно."""
    return list(range(low, high + 1))
def around(number, target, deviation):
    """Проверяет, находится ли number в диапазоне [target-deviation, target+deviation] (включительно)."""
    return target - deviation <= number <= target + deviation

def countdown(время):
    время += 1
    словарь = list(range(время))
    словарь = словарь[::-1]
    for i in словарь:
        time.sleep(1)
        время = str(время)
        длина = len(время)
        print(f"\r{i:>{длина}}", end = '\r', flush = True)