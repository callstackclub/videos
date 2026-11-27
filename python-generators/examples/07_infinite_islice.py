from itertools import islice
def naturals():
    n = 1
    while True:
        yield n
        n += 1
print(list(islice(naturals(), 5)))