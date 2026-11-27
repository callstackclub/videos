# Python decorators, built step by step

▶ **Watch:** https://youtu.be/12x2Ku8-syE

## In the video

1. The warm-up question
2. Question two: do it by hand
3. Question three: what does @ add?
4. Question four: any function at all
5. Question five: who are you?
6. A practical break
7. Question six: brackets
8. Question seven: the one people get backwards

## Key facts (checked for the video)

- @decorator above a def is the same as fn = decorator(fn) right after the def.
- functools.wraps copies the name, docstring and other attributes from the wrapped function to the wrapper.
- Stacked decorators are applied bottom-up at definition time.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`01_functions_are_objects.py`](examples/01_functions_are_objects.py): Passing and returning functions

Output:

```text
HI
8
```

### [`02_manual_decoration.py`](examples/02_manual_decoration.py): A decorator written by hand

Output:

```text
hello!
```

### [`03_at_syntax.py`](examples/03_at_syntax.py): The @ syntax

Output:

```text
hello!
```

### [`04_forwarding_arguments.py`](examples/04_forwarding_arguments.py): Forwarding any arguments

Output:

```text
calling
5
```

### [`05_name_is_lost.py`](examples/05_name_is_lost.py): Losing `__name__` without wraps

Output:

```text
wrapper
```

### [`06_wraps_preserves_metadata.py`](examples/06_wraps_preserves_metadata.py): Restoring metadata with wraps

Output:

```text
greet
Say hello.
```

### [`07_decorator_factory.py`](examples/07_decorator_factory.py): A decorator with an argument

Output:

```text
hahaha
```

### [`08_stacked_order.py`](examples/08_stacked_order.py): Stacked decorator order

Output:

```text
apply bottom
apply top
enter top
enter bottom
job
exit bottom
exit top
```

### [`count_calls.py`](examples/count_calls.py): A decorator with a memory

Output:

```text
call 1
call 2
7
```

### [`cache.py`](examples/cache.py): A ready-made one: cache

Output:

```text
working
16
16
```
