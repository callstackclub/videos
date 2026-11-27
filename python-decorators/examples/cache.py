from functools import cache

@cache
def square(n):
    print("working")
    return n * n

print(square(4))
print(square(4))
