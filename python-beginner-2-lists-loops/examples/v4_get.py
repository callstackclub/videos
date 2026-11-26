menu = {"tea": 2, "cake": 4}
order = ["tea", "pizza"]
for item in order:
    price = menu.get(item)
    if price is None:
        print(item, "- sorry, sold out")
    else:
        print(item, price)
