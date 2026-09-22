# Binary Search

## Recognition signals
- Sorted (or monotonic-answer) search space
- "Find first/last position", "minimum X such that condition holds" -->
  binary search on the answer, not just on an array

## Template
```python
lo, hi = 0, len(nums) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        ...
    elif nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
```

Binary search on the answer:
```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1
```

## Common pitfalls
- `lo <= hi` vs `lo < hi` mismatch with how `lo`/`hi` are updated (infinite loop)
- Integer overflow mid calc in other languages (not an issue in Python)
- Forgetting binary search applies to monotonic predicates, not just sorted arrays

## Linked problems
- (add slugs as you tag/confirm them)
