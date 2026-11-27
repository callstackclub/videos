# Python names, objects and the mutable default trap

▶ **Watch:** https://youtu.be/iRSUU8Vwl_0

## In the video

1. The call comes in
2. Clue one: names are labels
3. Clue three: when does the default happen?
4. The arrest
5. A second victim: copies
6. Case closed

## Key facts (checked for the video)

- Default argument values are evaluated once, when the def statement runs, not on every call.
- is compares object identity; == calls `__eq__` to compare values.
- copy.copy makes a shallow copy (nested objects are shared); copy.deepcopy copies nested objects too.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`assignment_binds_names.py`](examples/assignment_binds_names.py): Assignment binds another name

Output:

```text
[1, 2]
True
```

### [`identity_vs_equality.py`](examples/identity_vs_equality.py): Identity is not equality

Output:

```text
True
False
```

### [`default_evaluated_once.py`](examples/default_evaluated_once.py): Defaults are evaluated once

Output:

```text
default evaluated
definition finished
[]
[]
```

### [`mutable_default_shared.py`](examples/mutable_default_shared.py): The mutable default trap

Output:

```text
['a']
['a', 'b']
```

### [`none_default_fix.py`](examples/none_default_fix.py): Fix the default with None

Output:

```text
['a']
['b']
```

### [`shallow_copy_shares_nested.py`](examples/shallow_copy_shares_nested.py): A shallow copy shares nested lists

Output:

```text
[[1, 2]]
False
True
```

### [`deepcopy_copies_nested.py`](examples/deepcopy_copies_nested.py): A deep copy copies nested lists

Output:

```text
[[1]]
[[1, 2]]
False
```
