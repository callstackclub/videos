with open("list.txt", "w") as f:
    f.write("milk\nbread\n")
with open("list.txt") as f:
    for line in f:
        print(line.strip())
print(f.closed)
