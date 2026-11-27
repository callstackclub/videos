def count(fn):
    calls = 0
    def wrapper(*args):
        nonlocal calls
        calls += 1
        print("call", calls)
        return fn(*args)
    return wrapper

@count
def add(a, b):
    return a + b

add(1, 2)
print(add(3, 4))
