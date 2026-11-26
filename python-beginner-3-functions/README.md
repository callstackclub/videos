# Python for Beginners #3: Functions and Errors

▶ **Watch:** https://youtu.be/gP8WcAm88F8

## In the video

1. The review request
2. Comment one: you wrote this twice
3. Comment two: print isn't an answer
4. Comment three: make the calls readable
5. Comment four: that name doesn't exist out here
6. Comment five: somebody already wrote this
7. Comment six: the bad input
8. Approved

## Key facts (checked for the video)

- A function that does not return anything returns None.
- Variables assigned inside a function are local to it unless declared global.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`copies.py`](examples/copies.py): The till, copied twice

Output:

```text
6 8
```

### [`function.py`](examples/function.py): One function, used twice

Output:

```text
6
8
```

### [`print_only.py`](examples/print_only.py): Printing is not returning

Output:

```text
6
saved: None
```

### [`returned.py`](examples/returned.py): Returned, so it can be saved

Output:

```text
saved: 6
```

### [`default.py`](examples/default.py): A default value

Output:

```text
6
7
8
```

### [`keywords.py`](examples/keywords.py): Name your arguments

Output:

```text
tea 2 hot=True
cake 4 hot=False
```

### [`local.py`](examples/local.py): A variable that stays inside

Output:

```text
6
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 6, in <module>
    print(total)
          ^^^^^
NameError: name 'total' is not defined
```

### [`imports.py`](examples/imports.py): Borrow from the library

Output:

```text
8
7
```

### [`crash.py`](examples/crash.py): A customer types a word

Output:

```text
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 1, in <module>
    coins = int("three")
ValueError: invalid literal for int() with base 10: 'three'
```

### [`try_except.py`](examples/try_except.py): Catch the error you expect

Output:

```text
5
0
```

### [`too_wide.py`](examples/too_wide.py): A net that catches too much

Output:

```text
0
```

### [`else_finally.py`](examples/else_finally.py): else and finally

Output:

```text
thanks for 5
next customer
please type a number
next customer
```

### [`final.py`](examples/final.py): The reviewed till

Output:

```text
due 5, change 5
```
