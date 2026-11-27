# Python for Beginners #2: Loops and Lists

▶ **Watch:** https://youtu.be/6hiO5DmX_58

## In the video

1. Opening day
2. Version one: remember the order
3. Version two: read it back
4. Version three: know the prices
5. Version four: survive the pizza
6. Version five: a discount that lies
7. Versions six and seven: money and slices
8. Doors open

## Key facts (checked for the video)

- List and string indexes start at 0, and negative indexes count from the end.
- Reading a missing dictionary key with [] raises KeyError, while get returns None (or a default you give).

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`v1_list.py`](examples/v1_list.py): Version 1: an order is a list

Output:

```text
tea
coffee
3
True
```

### [`v1_crash.py`](examples/v1_crash.py): Crash 1: one step too far

Output:

```text
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 2, in <module>
    print(order[3])
          ~~~~~^^^
IndexError: list index out of range
```

### [`v2_loop.py`](examples/v2_loop.py): Version 2: print every line

Output:

```text
- tea
- cake
- coffee
0
1
2
```

### [`v3_prices.py`](examples/v3_prices.py): Version 3: a price list

Output:

```text
Total: 9
```

### [`v3_crash.py`](examples/v3_crash.py): Crash 2: not on the menu

Output:

```text
tea 2
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 4, in <module>
    print(item, menu[item])
                ~~~~^^^^^^
KeyError: 'pizza'
```

### [`v4_get.py`](examples/v4_get.py): Version 4: sold out

Output:

```text
tea 2
pizza - sorry, sold out
```

### [`v5_discount.py`](examples/v5_discount.py): Version 5: a discount

Output:

```text
Pay: 8
```

### [`v5_bug.py`](examples/v5_bug.py): The quiet bug: order matters

Output:

```text
Pay: 11
```

### [`v6_coins.py`](examples/v6_coins.py): Version 6: pay with coins

Output:

```text
paid so far: 3
paid so far: 6
paid so far: 9
change: 1
```

### [`v7_slices.py`](examples/v7_slices.py): Version 7: slices and tickets

Output:

```text
['tea', 'cake']
MIA
7
M
I
A
```

### [`final.py`](examples/final.py): The finished till

Output:

```text
tea 2
cake 4
pizza - sold out
coffee 3
Pay: 8
menu: tea 2
menu: cake 4
menu: coffee 3
```
