# Sliding Window

## Recognition signals
- Contiguous subarray/substring with a constraint (max/min length, sum,
  distinct chars, at most K of something)
- Brute force would be O(n^2) re-scanning; window state can be updated
  incrementally instead

## Template
```python
left = 0
window_state = {}
best = 0
for right, val in enumerate(nums):
    # expand: add val to window_state
    while <window invalid>:
        # shrink: remove nums[left] from window_state
        left += 1
    best = max(best, right - left + 1)
```

## Common pitfalls
- Confusing "at most K" with "exactly K" (exactly K = atMost(K) - atMost(K-1))
- Shrinking the window with the wrong condition (off-by-one on `<` vs `<=`)
- Not resetting/decrementing window state correctly when the left pointer moves

## Linked problems
- (add slugs as you tag/confirm them)
