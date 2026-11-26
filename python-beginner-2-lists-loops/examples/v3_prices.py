menu = {"tea": 2, "cake": 4}
menu["coffee"] = 3
order = ["tea", "cake", "coffee"]
total = 0
for item in order:
    total = total + menu[item]
print("Total:", total)
