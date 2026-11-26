to_pay = 8
paid = 0
while True:
    paid = paid + 3
    print("paid so far:", paid)
    if paid >= to_pay:
        break
print("change:", paid - to_pay)
