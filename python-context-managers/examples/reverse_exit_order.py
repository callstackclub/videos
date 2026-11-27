from contextlib import contextmanager

@contextmanager
def bag(name):
    print("open", name)
    yield
    print("close", name)

with bag("A"), bag("B"):
    print("pack groceries")