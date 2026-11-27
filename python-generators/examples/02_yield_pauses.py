log = []
def gen():
    n = 10
    log.append('at first yield')
    yield n
    log.append('resumed')
    n += 5
    yield n
g = gen()
print(next(g), log)
print(next(g), log)