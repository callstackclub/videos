def log_call(fn):
    def wrapper(*args, **kwargs):
        print('calling')
        return fn(*args, **kwargs)
    return wrapper

@log_call
def add(a, b=0):
    return a + b

print(add(2, b=3))