def read_coins(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(read_coins("5"))
print(read_coins("three"))
