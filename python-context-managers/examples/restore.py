from contextlib import contextmanager

settings = {"lang": "en"}

@contextmanager
def language(new):
    old = settings["lang"]
    settings["lang"] = new
    try:
        yield
    finally:
        settings["lang"] = old

with language("ms"):
    print(settings["lang"])
print(settings["lang"])
