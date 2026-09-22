# Two Pointers

## Recognition signals
- Sorted array (or can be sorted without losing needed info)
- Looking for a pair/triplet satisfying a sum/difference condition
- Need to compare elements from both ends, or a fast/slow pair moving through
  one sequence

## Template
```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        ...
    elif total < target:
        left += 1
    else:
        right -= 1
```

## Common pitfalls
- Forgetting to skip duplicates when the problem wants unique combinations
  (3Sum-style)
- Using two pointers on unsorted data without realizing sortedness was load-bearing
- Off-by-one on the `while left < right` vs `<=` boundary

## Linked problems
- (add slugs as you tag/confirm them, e.g. `two-sum-less-than-k`, `3sum`)
