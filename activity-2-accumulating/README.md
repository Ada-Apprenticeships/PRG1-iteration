# Activity 2: Accumulating

File: `accumulating.py`

## Predict

- What does `total_of([12, 7, 19, 3])` return?
- What does `total_of([])` return?
- What does `largest_of([12, 7, 19, 3])` return?

## Run

Execute and compare.

## Investigate

- `total` starts at 0. Trace what it holds after each pass of the loop. Write the
  four values down.
- What would `total_of([12, 7, 19, 3])` return if `total` started at 1 instead?
  Predict the exact number, then try it.
- `largest_of` starts `biggest` at `numbers[0]` rather than at 0. Why? What would
  go wrong with a starting value of 0 if every reading were negative?
- `total_of([])` returns 0 without any special handling. Does `largest_of([])`
  behave as well? Try it and see what happens.

## Modify

- Change `total_of` so it adds up only the numbers above 10.
- Change `largest_of` into `smallest_of`. Which parts have to change, and which
  do not?

> Where an accumulator starts is a decision, not a detail. Starting a total at 0
> and a maximum at the first item are both deliberate, and both go wrong quietly
> when copied to the wrong situation.
