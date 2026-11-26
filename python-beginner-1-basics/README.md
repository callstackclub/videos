# Python for Beginners #1: Variables and Types

▶ **Watch:** https://youtu.be/O2mn8UwfahA

## In the video

1. The rules of the game
2. Rounds one and two: names
3. Rounds three to five: what kind of thing?
4. Rounds six and seven: numbers with opinions
5. Rounds eight and nine: changing type on purpose
6. Round ten: the space that matters
7. Final score

## Key facts (checked for the video)

- In Python, // is floor division and / always gives a float.
- % gives the remainder of a division.
- Blocks in Python are defined by indentation.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`names.py`](examples/names.py): A name or the text?

Output:

```text
Mia
name
```

### [`relabel.py`](examples/relabel.py): Moving a label

Output:

```text
8 10
```

### [`types.py`](examples/types.py): Ask for the type

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### [`plus.py`](examples/plus.py): Two kinds of plus

Output:

```text
22
4
```

### [`mix.py`](examples/mix.py): Text plus number

Output:

```text
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 2, in <module>
    print("Score: " + score)
          ~~~~~~~~~~^~~~~~~
TypeError: can only concatenate str (not "int") to str
```

### [`fstring.py`](examples/fstring.py): Three ways to write it

Output:

```text
Score: 8
Mia scored 8
{name} scored {score}
```

### [`divide.py`](examples/divide.py): Three kinds of division

Output:

```text
4.0
3
2
3.4
```

### [`decimals.py`](examples/decimals.py): A famous decimal surprise

Output:

```text
0.30000000000000004
0.3
```

### [`to_int.py`](examples/to_int.py): Text into a number

Output:

```text
19
3
```

### [`bad_int.py`](examples/bad_int.py): Not a number

Output:

```text
Traceback (most recent call last):
  File "/home/mia/demo/main.py", line 2, in <module>
    number = int(text)
ValueError: invalid literal for int() with base 10: 'abc'
```

### [`if_block.py`](examples/if_block.py): What belongs to the if?

Output:

```text
Done
```

### [`no_indent.py`](examples/no_indent.py): A missing indent

Output:

```text
File "/home/mia/demo/main.py", line 3
    print("You can vote.")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```
