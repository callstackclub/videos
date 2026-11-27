class Door:
    def __enter__(self):
        print("open")
    def __exit__(self, *exc):
        print("close")
try:
    with Door():
        raise ValueError("bad milk")
except ValueError as error:
    print("caught:", error)