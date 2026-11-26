def bill(prices, tip=0):
    return sum(prices) + tip

print(bill([2, 4]))
print(bill([2, 4], 1))
print(bill([2, 4], tip=2))
