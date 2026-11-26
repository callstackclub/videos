def label(item, price, hot):
    return f"{item} {price} hot={hot}"

print(label("tea", 2, True))
print(label(hot=False, price=4, item="cake"))
