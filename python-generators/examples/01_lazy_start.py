events = []
def gen():
    events.append('body ran')
    yield 1
g = gen()
print('after call:', type(g).__name__, events)
print('first next:', next(g))
print('after next:', events)