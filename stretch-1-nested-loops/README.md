# Stretch 1: Nested loops

File: `nested.py`

Optional. Only if you have finished the four core activities.

Nested loops are covered properly later in the module, with 2D data. This is a
first look, and the only question being asked is how many times things run.

## Predict

- How many lines does the multiplication table print, not counting the blank
  ones? Work it out, do not count the output.
- What is the final value of `total_printed`?

## Run

Execute and compare.

## Investigate

- The outer loop runs 3 times and the inner loop runs 3 times. The inner body
  runs 9. Where does 9 come from, and what would it be if the outer loop ran 5
  times and the inner ran 4?
- The blank `print()` sits inside the outer loop but outside the inner one. How
  can you tell that from reading, and what would change if it were indented one
  level further?
- In the second example, `total_printed` is declared before both loops rather
  than inside either. What would happen if it were set to 0 at the top of the
  outer loop instead? Predict, then try it.

## Modify

- Change the table to go up to 5 by 5, and predict the new line count first.
- Make the table print only the rows where `row` is even.
