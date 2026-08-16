import shutil as sh
import time
x, y = sh.get_terminal_size()

def head(obj='='):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(obj * x)
            print(' '*int(x/2), end='')
            func(*args, **kwargs)
            print(obj * x)
        return wrapper
    return decorator

def new_text(sep='='):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(sep * x)
            func(*args, **kwargs)
        return wrapper
    return decorator

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{elapsed:.4f}")
        return result
    return wrapper