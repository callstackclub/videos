def decorate(fn):
    def wrapper():
        return fn()
    return wrapper

@decorate
def greet():
    return 'hi'

print(greet.__name__)