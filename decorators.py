import time
from functools import wraps

cache = {}


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper


def cache_args(func):
    cache_dict = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper


@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


print(long_heavy(1))
# Время выполнения функции long_heavy: 1.0 с.
# 2
print(long_heavy(1))
# Время выполнения функции long_heavy: 0.0 с.
# 2
print(long_heavy(2))
# Время выполнения функции long_heavy: 1.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 4





def cache3(func):
    cache = {'count': 0}
    #@wraps(func)
    def wrapper(*args):
        if cache['count'] == 0:
            cache[args] = func(*args)
            cache['count'] += 1
            #print('КЭШ:', cache['count'])
            return cache[args]
        else:
            cache['count'] += 1
            #print('КЭШ:', cache['count'])
            if cache['count'] == 3:
                cache['count'] = 0
            return cache[args]
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1