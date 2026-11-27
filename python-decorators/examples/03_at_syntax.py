def exclaim(fn):
    def wrapper():
        return fn() + '!'
    return wrapper

@exclaim
def greet():
    return 'hello'

print(greet())