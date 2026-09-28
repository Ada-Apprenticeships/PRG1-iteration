# Activity 4: Broken loops

File: `broken_loops.py`

Three faults. Nothing crashes, nothing hangs, and every output looks plausible.

## Predict

Work out what each call **should** produce:

- `count_to(5)` should print the numbers 1 to 5.
- `total_of([12, 7, 19, 3])` should give the sum of those four numbers.
- A courier gets three attempts to deliver a parcel. If nobody answers by the
  third, it goes back to the depot. The call supplies five days of no answer.

## Run

Execute it.

## Investigate

The first two faults announce themselves if you counted properly. The third does
not, and it is the important one.

- `count_to(5)` printed four numbers. Which end of the `range` is wrong?
- `total_of` returned 42. Add the four numbers yourself. What is the difference,
  and where did it come from?
- `delivery_outcome` printed "Returned to depot", which is what you expected.
  **Count how many attempts it actually made before saying so.** Add a `print`
  inside the loop if that helps. Was it three?

## Fault log

You will fill in exactly this, marked, in Task 2 this afternoon.

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. After fixing, `count_to(5)` prints 1 to 5, `total_of` returns 41,
and `delivery_outcome` gives up after the third attempt, not the fourth.

> The third fault is the one to remember. A courier making a fourth attempt when
> the contract allows three costs real money on every parcel, it produces exactly
> the message you expected, and no test you have not written will tell you about
> it. The same off-by-one on a limit turns up everywhere, including in Task 2.
