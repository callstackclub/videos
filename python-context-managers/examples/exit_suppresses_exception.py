class Door:
    def __enter__(self):
        return self
    def __exit__(self, kind, error, tb):
        print("exit saw:", kind.__name__)
        return True

with Door():
    raise ValueError("bad milk")
print("program continues")