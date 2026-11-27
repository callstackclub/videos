class Door:
    def __enter__(self):
        print("open")
    def __exit__(self, *exc):
        print("close")

with Door():
    print("inside")