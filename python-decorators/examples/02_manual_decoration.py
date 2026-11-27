def exclaim(fn):
    def wrapper():
        return fn() + '!'
    return wrapper

def greet():
    return 'hello'

greet = exclaim(greet)
print(greet())