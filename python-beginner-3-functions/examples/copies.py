menu = {"tea": 2, "cake": 4}
total_a = 0
for item in ["tea", "cake"]:
    total_a = total_a + menu.get(item, 0)
total_b = 0
for item in ["cake", "cake"]:
    total_b = total_b + menu.get(item, 0)
print(total_a, total_b)
