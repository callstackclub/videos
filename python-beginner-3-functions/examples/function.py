menu = {"tea": 2, "cake": 4}

def bill(order):
    total = 0
    for item in order:
        total = total + menu.get(item, 0)
    return total

print(bill(["tea", "cake"]))
print(bill(["cake", "cake"]))
