menu = {"tea": 2, "cake": 4}

def bill(order, discount=0):
    total = 0
    for item in order:
        total = total + menu.get(item, 0)
    return total - discount

def read_coins(text):
    try:
        return int(text)
    except ValueError:
        return 0

due = bill(["tea", "cake"], discount=1)
paid = read_coins("10")
print(f"due {due}, change {paid - due}")
