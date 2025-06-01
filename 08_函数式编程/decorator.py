# 装饰漆
import functools
from datetime import datetime

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s: %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("现在是：%s" % datetime.now())

now()
print(now.__name__)