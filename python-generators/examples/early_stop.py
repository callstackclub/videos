def prices():
    for p in [2, 45, 12]:
        print("made", p)
        yield p

for p in prices():
    if p > 40:
        print("found", p)
        break
