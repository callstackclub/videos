from functools import wraps

def decorate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@decorate
def greet():
    '''Say hello.'''
    return 'hi'

print(greet.__name__)
print(greet.__doc__)