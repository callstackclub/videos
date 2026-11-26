fruits = ["fig", "kiwi", "fig"]
counts = {}
for f in fruits:
    counts[f] = counts.get(f, 0) + 1
print(counts["fig"])
