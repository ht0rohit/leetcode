# Dynamic Programming

## Recognition signals
- "Number of ways", "min/max cost", "can you reach/partition" over a sequence
  or grid with overlapping subproblems
- Brute-force recursion re-solves the same subproblem repeatedly

## Approach checklist
1. Define the state precisely (what does `dp[i]` or `dp[i][j]` mean?)
2. Find the recurrence (how does the state relate to smaller states?)
3. Base cases
4. Order of computation (bottom-up) or memoize (top-down)
5. Can space be compressed (rolling array)?

## Common pitfalls
- Vague state definition ("dp[i] = the answer" is not precise enough)
- Off-by-one between 0-indexed array and 1-indexed dp table
- Missing a base case that only shows up for small/edge inputs

## Linked problems
- (add slugs as you tag/confirm them)
