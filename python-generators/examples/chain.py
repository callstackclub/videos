lines = ["tea 2", "", "cake 4"]
full = (x for x in lines if x)
prices = (int(x.split()[1]) for x in full)
print(sum(prices))
