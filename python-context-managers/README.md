# Python context managers: what with really does

▶ **Watch:** https://youtu.be/1me1IpYW7zQ

## In the video

1. Six claims on the table
2. Claim 1: it only works on files
3. Claims 2 and 3: when the block fails
4. Claim 4: you have to write a class
5. Claim 5: the trap
6. Claim 6: the closing order
7. After the trial: two you can use today
8. The verdicts

## Key facts (checked for the video)

- If `__exit__` returns a true value, the exception raised in the with block is suppressed.
- Managers in one with statement are exited in reverse order.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`enter_exit_normal.py`](examples/enter_exit_normal.py): `__enter__` and `__exit__` on a normal block

Output:

```text
open
inside
close
```

### [`exit_on_error.py`](examples/exit_on_error.py): `__exit__` runs when the block raises

Output:

```text
open
close
caught: bad milk
```

### [`exit_receives_exception.py`](examples/exit_receives_exception.py): `__exit__` receives the exception

Output:

```text
ValueError bad milk
not suppressed
```

### [`exit_suppresses_exception.py`](examples/exit_suppresses_exception.py): Returning True suppresses the exception

Output:

```text
exit saw: ValueError
program continues
```

### [`contextmanager_yield.py`](examples/contextmanager_yield.py): Write a manager with @contextmanager

Output:

```text
take list
['milk', 'bread']
put list away
```

### [`contextmanager_finally.py`](examples/contextmanager_finally.py): Use try/finally around yield

Output:

```text
take list
put list away
caught: bad milk
```

### [`reverse_exit_order.py`](examples/reverse_exit_order.py): Two managers exit in reverse order

Output:

```text
open A
open B
pack groceries
close B
close A
```

### [`restore.py`](examples/restore.py): Change a setting, then put it back

Output:

```text
ms
en
```

### [`suppress.py`](examples/suppress.py): A ready-made one: suppress

Output:

```text
carried on
```
