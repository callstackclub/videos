def repeat(times):
    def decorator(fn):
        def wrapper():
            return fn() * times
        return wrapper
    return decorator

@repeat(3)
def laugh():
    return 'ha'

print(laugh())