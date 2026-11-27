def make_default():
    print("default evaluated")
    return []

def get_default(value=make_default()):
    return value

print("definition finished")
print(get_default())
print(get_default())