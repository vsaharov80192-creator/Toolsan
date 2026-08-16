from .new import calculate
class MathError(Exception):
    pass
def _extract_numbers(numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        return list(numbers[0])
    return list(numbers)
    
def calc(prompt, tp):
    try:
        return tp(calculate(prompt))
    except:
        raise MathError(f"Invalid type") from None

def armean(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], list):
        numbers = numbers[0]
    else:
        numbers = list(numbers)
    
    return sum(numbers) / len(numbers)

def median(*numbers):
    data = _extract_numbers(numbers)
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    return (data[n // 2 - 1] + data[n // 2]) / 2

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def lerp(a, b, t):
    return a + (b - a) * t

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def linspace(start, stop, num=50):
    if num <= 0:
        return []
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]

def arange(start, stop, step=1):
    result = []
    current = start
    while current < stop:
        result.append(current)
        current += step
    return result

def dot(a, b):
    if len(a) != len(b):
        raise MathError("The vectors have different lengths.")
    return sum(a[i] * b[i] for i in range(len(a)))

def norm(a):
    return sum(x ** 2 for x in a) ** 0.5

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

def quantile(data, q):
    sorted_data = sorted(data)
    n = len(sorted_data)
    idx = q * (n - 1)
    if idx.is_integer():
        return sorted_data[int(idx)]
    lo = int(idx)
    hi = lo + 1
    return sorted_data[lo] + (sorted_data[hi] - sorted_data[lo]) * (idx - lo)

def iqr(data):
    return quantile(data, 0.75) - quantile(data, 0.25)

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def matmul(A, B):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    if cols_a != rows_b:
        raise MathError("Cannot multiply: cols(A) != rows(B)")
    return [[sum(A[i][k] * B[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]