# Python for Beginners #4: 10 Tips and Tricks

▶ **Watch:** https://youtu.be/QAgK55hbr5k

## In the video

1. Ring the bell
2. Rounds 1 to 3: loops
3. Rounds 4 to 6: moving things around
4. Rounds 7 and 8: answers about a whole list
5. Rounds 9 and 10: text
6. The scorecard

## Key facts (checked for the video)

- zip stops at the shortest input.
- enumerate starts counting at 0 unless you give a start.
- A Counter counts how often each value appears.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`long_filter.py`](examples/long_filter.py): The long way

Output:

```text
[2, 4]
```

### [`short_filter.py`](examples/short_filter.py): The Python way

Output:

```text
[2, 4]
```

### [`long_place.py`](examples/long_place.py): Counting by hand

Output:

```text
1 Ana
2 Ben
3 Cy
```

### [`short_place.py`](examples/short_place.py): enumerate

Output:

```text
1 Ana
2 Ben
3 Cy
```

### [`zip_pairs.py`](examples/zip_pairs.py): zip

Output:

```text
Ana 90
Ben 75
```

### [`long_swap.py`](examples/long_swap.py): A third box

Output:

```text
2 1
```

### [`short_swap.py`](examples/short_swap.py): One line

Output:

```text
2 1
```

### [`unpack.py`](examples/unpack.py): Take the first, keep the rest

Output:

```text
10
[20, 30]
```

### [`sort_key.py`](examples/sort_key.py): Sort your way

Output:

```text
['apple', 'banana', 'fig']
['fig', 'apple', 'banana']
['banana', 'apple', 'fig']
['banana', 'fig', 'apple']
```

### [`split_join.py`](examples/split_join.py): split and join

Output:

```text
['milk', 'bread', 'eggs']
milk + bread + eggs
```

### [`any_all.py`](examples/any_all.py): any, all and sum

Output:

```text
227
True
False
```

### [`long_count.py`](examples/long_count.py): Count with get

Output:

```text
2
```

### [`short_count.py`](examples/short_count.py): Count with Counter

Output:

```text
2
0
```

### [`fstring.py`](examples/fstring.py): f-string formatting

Output:

```text
3.14
[   tea]
name='tea'
```

### [`slicing.py`](examples/slicing.py): Slicing

Output:

```text
desserts
str
sed
```

### [`with_open.py`](examples/with_open.py): with open

Output:

```text
milk
bread
True
```
