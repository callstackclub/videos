def letters():
    yield 'a'
    yield 'b'
for letter in letters():
    print(letter)
print('loop finished normally')