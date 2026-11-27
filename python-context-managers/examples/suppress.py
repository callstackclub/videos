from contextlib import suppress

with suppress(ValueError):
    int("abc")
    print("never printed")
print("carried on")
