from contextlib import contextmanager

@contextmanager
def shopping():
    print("take list")
    yield ["milk", "bread"]
    print("put list away")

with shopping() as items:
    print(items)