def pay(text):
    try:
        coins = int(text)
    except ValueError:
        print("please type a number")
    else:
        print("thanks for", coins)
    finally:
        print("next customer")

pay("5")
pay("three")
