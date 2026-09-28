# Activity 3: While, and stopping

File: `stopping.py`

## Predict

- What does `countdown(3)` print, line by line?
- What does `countdown(0)` print? Does the loop body run at all?
- What do the two `first_over` calls return?

## Run

Execute and compare. `countdown(0)` catches most people.

## Investigate

- `countdown` checks its condition **before** running the body. That is why
  `countdown(0)` behaves as it does. Explain it to your partner in one sentence.
- Delete the line `count = count - 1` and predict what happens. **Do not run it**
  until you have said out loud what you expect. Then run it, and press Ctrl+C to
  stop it.
- `first_over` has two ways of finishing: it finds something, or it runs out.
  Which line handles each? What does it return when it runs out?
- Every loop has at least one way out. How many does `first_over` have, and how
  many does `countdown` have?

## Modify

- Rewrite `countdown` as a `for` loop with `range`. Which version reads better,
  and why?
- Change `first_over` so it returns how many readings it checked before finding
  one, rather than the reading itself.

## Make (stretch)

Optional. Only if you have finished everything above.

Write a loop with exactly two ways out, one of them early. Then write down, in a
comment above it, what each route means in plain English. If you cannot describe
both in a sentence each, the loop is probably doing too much.

> A loop you cannot see the exit from is a loop you do not understand yet. When
> you read one, find every route out before you do anything else.
