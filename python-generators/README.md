# Python generators: lazy values with yield

▶ **Watch:** https://youtu.be/V1Zi-sPQ4sY

## In the video

1. Opening the notebook
2. Experiments 1 and 2: the sleeping function
3. Experiments 3 and 4: the end of the road
4. Experiments 5 and 6: short form, single use
5. Experiment 7: endless on purpose
6. Field tests
7. Conclusions

## Key facts (checked for the video)

- Calling a generator function returns a generator object and runs none of the body.
- A generator can be iterated only once; a second pass yields nothing.
- Returning from a generator (or reaching its end) raises StopIteration, and a for loop stops on it.

## Examples

Every example below was run before it was shown in the video. Run one with `python examples/<file>.py`.

### [`01_lazy_start.py`](examples/01_lazy_start.py): Generator bodies start lazily

Output:

```text
after call: generator []
first next: 1
after next: ['body ran']
```

### [`02_yield_pauses.py`](examples/02_yield_pauses.py): yield pauses and preserves locals

Output:

```text
10 ['at first yield']
15 ['at first yield', 'resumed']
```

### [`03_stop_iteration.py`](examples/03_stop_iteration.py): Exhaustion raises StopIteration

Output:

```text
only
StopIteration: generator finished
```

### [`04_for_loop_stops.py`](examples/04_for_loop_stops.py): for handles generator exhaustion

Output:

```text
a
b
loop finished normally
```

### [`05_generator_expression.py`](examples/05_generator_expression.py): Generator expression syntax

Output:

```text
generator
[0, 1, 4, 9]
```

### [`06_single_use.py`](examples/06_single_use.py): Generators can be consumed only once

Output:

```text
first pass: [0, 1, 4]
second pass: []
```

### [`07_infinite_islice.py`](examples/07_infinite_islice.py): Slice an infinite generator

Output:

```text
[1, 2, 3, 4, 5]
```

### [`08_yield_from.py`](examples/08_yield_from.py): Delegate with yield from

Output:

```text
[0, 1, 2, 3]
```

### [`early_stop.py`](examples/early_stop.py): Stop early, skip the work

Output:

```text
made 2
made 45
found 45
```

### [`chain.py`](examples/chain.py): Generators in a chain

Output:

```text
6
```
