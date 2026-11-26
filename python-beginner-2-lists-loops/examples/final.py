menu = {"tea": 2, "cake": 4, "coffee": 3}
order = ["tea", "cake", "pizza", "coffee"]
total = 0
for item in order:
    price = menu.get(item)
    if price is None:
        print(item, "- sold out")
    else:
        print(item, price)
        total = total + price
if total >= 5:
    total = total - 1
print("Pay:", total)
for item, price in menu.items():
    print("menu:", item, price)
