# Stretch 2: enumerate and zip

File: `pairing.py`

Optional. Only if you have finished the four core activities.

Two tools you will see in other people's loops long before you need to write
them yourself. Read them here so they are not a surprise later.

## Predict

Three blocks, separated by dashed lines. Write down the output of each before
running. The third block is the interesting one.

## Run

Execute and compare.

## Investigate

- `enumerate` gives you two things on each pass instead of one. What are they,
  and which one starts at 0?
- `zip` walks two lists together. What is the rule for what it pairs up?
- The third block zips a list of two names against a list of three ages. It does
  not crash and it does not warn you. What happened to the third age? Why might
  that be a fault waiting to happen rather than a convenience?

## Modify

- Rewrite the first block using `range` and indexing instead of `enumerate`.
  Which version is easier to read, and which is easier to get wrong?
- Make the third block print something sensible about the age with no matching
  name, rather than silently dropping it.

> `zip` stopping at the shorter list is the behaviour people forget. If the two
> lists are supposed to be the same length, a silent truncation is exactly the
> kind of fault that survives testing.
