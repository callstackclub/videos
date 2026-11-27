from contextlib import contextmanager

@contextmanager
def shopping():
    print("take list")
    try:
        yield ["milk", "bread"]
    finally:
        print("put list away")

try:
    with shopping():
        raise ValueError("bad milk")
except ValueError as error:
    print("caught:", error)