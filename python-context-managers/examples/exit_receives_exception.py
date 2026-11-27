class Door:
    def __enter__(self):
        return self
    def __exit__(self, kind, error, tb):
        print(kind.__name__, error)
try:
    with Door():
        raise ValueError("bad milk")
except ValueError:
    print("not suppressed")