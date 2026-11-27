def shout(text):
    return text.upper()

def call(fn, value):
    return fn(value)

def make_adder(n):
    def add(x):
        return x + n
    return add

print(call(shout, 'hi'))
add_five = make_adder(5)
print(add_five(3))