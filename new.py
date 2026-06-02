import time
import sys
import os
import re
import random
import math

# ANSI color codes
BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, WHITE = (
    '\033[30m', '\033[31m', '\033[32m', '\033[33m',
    '\033[34m', '\033[35m', '\033[36m', '\033[37m'
)
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_PURPLE, BRIGHT_CYAN, BRIGHT_WHITE = (
    '\033[90m', '\033[91m', '\033[92m', '\033[93m',
    '\033[94m', '\033[95m', '\033[96m', '\033[97m'
)

BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_PURPLE, BG_CYAN, BG_WHITE = (
    '\033[40m', '\033[41m', '\033[42m', '\033[43m',
    '\033[44m', '\033[45m', '\033[46m', '\033[47m'
)
BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_BLUE, BG_BRIGHT_PURPLE, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE = (
    '\033[100m', '\033[101m', '\033[102m', '\033[103m',
    '\033[104m', '\033[105m', '\033[106m', '\033[107m'
)

BOLD, ITALIC, UNDERLINE, STRIKE = '\033[1m', '\033[3m', '\033[4m', '\033[9m'


# Core functions

def superprint(word, delay=0, color='', bg_color='', style='', end='\n'):
    """Print text letter by letter with ANSI colors and styles."""
    prefix = ''
    if style:
        prefix += style
    if color:
        prefix += color
    if bg_color:
        prefix += bg_color

    suffix = '\033[0m' if prefix else ''

    if prefix:
        sys.stdout.write(prefix)

    for ch in word:
        time.sleep(delay)
        sys.stdout.write(ch)
        sys.stdout.flush()

    if suffix:
        sys.stdout.write(suffix)

    print(end=end, flush=True)


def loadspin(seconds, speed=10, color=''):
    """Display a spinner animation for the given duration."""
    frames = ['|', '/', '-', '\\']
    start = time.perf_counter()
    i = 0

    if color:
        sys.stdout.write(color)

    while time.perf_counter() - start < seconds:
        sys.stdout.write(f"\r{frames[i % len(frames)]}")
        sys.stdout.flush()
        time.sleep(1 / speed)
        i += 1

    if color:
        sys.stdout.write('\033[0m')
    print()


def smart_input(prompt, typ=str, delay=0, color=''):
    """Print prompt letter by letter, then read input and convert to given type."""
    if color:
        sys.stdout.write(color)

    for ch in prompt:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write('\033[0m')
    user_input = input()

    try:
        return typ(user_input)
    except ValueError:
        return None


def bgcolor(color=None):
    """Set background color of the terminal (pass ANSI bg code) or reset."""
    if color:
        sys.stdout.write(f"{color}\033[2J\033[H\033[3J")
    else:
        sys.stdout.write("\033[0m\033[2J\033[H\033[3J")
    sys.stdout.flush()


def between(text, word, left, right):
    """Return True if `word` is between `left` and `right` in the text."""
    if isinstance(text, str):
        words = text.split()
    elif isinstance(text, list):
        words = text
    else:
        return False
    try:
        pos_left = words.index(left)
        pos_word = words.index(word)
        pos_right = words.index(right)
        return pos_left < pos_word < pos_right or pos_left > pos_word > pos_right
    except ValueError:
        return False


def calculate(expression):
    """
    Safe calculator with support for:
    - negative numbers
    - sin, cos (in degrees)
    - pi, e
    - log, log10, sqrt
    - ^, !, parentheses
    """
    try:
        expr = expression.strip()

        # Constants
        expr = expr.replace('pi', str(math.pi))
        expr = expr.replace('e', str(math.e))

        # Symbol replacements
        expr = expr.replace('×', '*').replace('•', '*').replace('x', '*').replace('х', '*')
        expr = expr.replace('÷', '/').replace(':', '/')
        expr = expr.replace('^', '**')
        expr = expr.replace(' ', '')

        # Unicode powers
        powers = {'²': '2', '³': '3', '⁴': '4', '⁵': '5'}
        for sym, num in powers.items():
            expr = expr.replace(sym, f'**{num}')

        # Factorial helper
        def factorial(n):
            if n < 0:
                return None
            if n == 0 or n == 1:
                return 1
            res = 1
            for i in range(2, int(n) + 1):
                res *= i
            return res

        # Fix unary minus
        def fix_unary_minus(e):
            if e.startswith('-'):
                e = '0' + e
            e = re.sub(r'\(-', '(0-', e)
            e = re.sub(r'([+\-*/])-', r'\1 0-', e)
            return e.replace(' ', '')

        # Parser
        def parse(e):
            e = fix_unary_minus(e)

            # sin, cos in degrees
            e = re.sub(r'sin\(([^()]+)\)', lambda m: str(math.sin(math.radians(float(parse(m.group(1)))))), e)
            e = re.sub(r'cos\(([^()]+)\)', lambda m: str(math.cos(math.radians(float(parse(m.group(1)))))), e)

            # sqrt
            e = re.sub(r'sqrt\(([^()]+)\)', lambda m: str(math.sqrt(float(parse(m.group(1))))), e)

            # log and log10
            e = re.sub(r'log\(([^()]+)\)', lambda m: str(math.log(float(parse(m.group(1))))), e)
            e = re.sub(r'log10\(([^()]+)\)', lambda m: str(math.log10(float(parse(m.group(1))))), e)

            # factorial
            e = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), e)

            # parentheses
            while '(' in e:
                e = re.sub(r'\(([^()]+)\)', lambda m: str(parse(m.group(1))), e)

            # fix double signs
            e = e.replace('--', '+').replace('+-', '-').replace('-+', '-')

            # power
            e = re.sub(r'([\d.]+)\*\*([\d.]+)', lambda m: str(float(m.group(1)) ** float(m.group(2))), e)

            # multiplication and division
            while re.search(r'[\d.]+[*/][\d.]+', e):
                e = re.sub(r'([\d.]+)([*/])([\d.]+)',
                           lambda m: str(float(m.group(1)) * float(m.group(3)) if m.group(2) == '*' else float(m.group(1)) / float(m.group(3))),
                           e)

            # addition and subtraction
            while re.search(r'[\d.]+[+\-][\d.]+', e):
                e = re.sub(r'([\d.]+)([+\-])([\d.]+)',
                           lambda m: str(float(m.group(1)) + float(m.group(3)) if m.group(2) == '+' else float(m.group(1)) - float(m.group(3))),
                           e)

            return e

        # Check if expression has any operators
        if not any(op in expr for op in ["+", "-", "*", "/", "**", "sin", "cos", "sqrt", "log", "(", "!"]):
            return None

        result = parse(expr)
        res = float(result)

        if res.is_integer():
            return int(res)
        return round(res, 10)

    except Exception:
        return None


def random_obj(lst):
    """Return a random element from the list."""
    return lst[random.randint(0, len(lst) - 1)]


def error(text): superprint(text, color=RED, style=BOLD)
def warn(text): superprint(text, color=YELLOW, style=BOLD)
def success(text): superprint(text, color=GREEN)
def info(text): superprint(text, color=BLUE)


def levenshtein(a, b):
    """Return the Levenshtein distance between two strings."""
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


def sim(word1, word2, threshold=0.6):
    """Check if two words are similar based on Levenshtein distance."""
    if not word1 or not word2:
        return False
    w1 = word1.lower()
    w2 = word2.lower()
    max_len = max(len(w1), len(w2))
    if max_len == 0:
        return True
    distance = levenshtein(w1, w2)
    ratio = 1 - (distance / max_len)
    return ratio >= threshold


def formatcheck(obj, typ):
    """Check if object is of given type."""
    return isinstance(obj, typ)


# Constants for order()
FIRST = 0
LAST = -1
RANDOM = "random"


def order(lst, key):
    """Return first, last or random element of the list."""
    if key == FIRST:
        return lst[FIRST]
    elif key == LAST:
        return lst[LAST]
    elif key == RANDOM:
        return random.choice(lst)
    return None


def timer(seconds, message):
    """Wait for given seconds and print a message."""
    time.sleep(seconds)
    print(message)


def flatten(*lists):
    """Concatenate several lists into one."""
    return sum(lists, [])


def integers_between(low, high):
    """Return list of integers from low to high inclusive."""
    return list(range(low, high + 1))


def around(number, target, deviation):
    """Check if number is within [target-deviation, target+deviation] inclusive."""
    return target - deviation <= number <= target + deviation


def countdown(seconds):
    """Display a countdown from seconds to 0 (seconds only, no minutes)."""
    for i in range(seconds, -1, -1):
        print(f"\r{i:>{len(str(seconds))}}", end='', flush=True)
        time.sleep(1)
    print()