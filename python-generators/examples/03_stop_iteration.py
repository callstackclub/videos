def one():
    yield 'only'
g = one()
print(next(g))
try:
    next(g)
except StopIteration:
    print('StopIteration: generator finished')