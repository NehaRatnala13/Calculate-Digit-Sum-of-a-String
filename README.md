# [2243. Calculate Digit Sum of a String](https://leetcode.com/problems/calculate-digit-sum-of-a-string/)

![Difficulty: Easy](https://shields.io)
![Topics: String, Simulation](https://shields.io)

## 📝 Problem Description
You are given a string `s` of digits and an integer `k`. As long as `s.length > k`, you repeatedly divide `s` into consecutive groups of length `k` (the last group may be smaller), replace each group with the sum of its digits, and concatenate the sums to form a new `s`. For full problem details and examples, refer to the [LeetCode Problem Page](https://leetcode.com/problems/calculate-digit-sum-of-a-string/).

### Constraints
* `1 <= s.length <= 100`
* `2 <= k <= 100`
* `s` consists of digits only.

---

## 💡 Approach & Complexity

### Simulation
We simulate the process using a `while` loop that continues while `len(s) > k`:
1. Slice `s` into consecutive chunks of size `k`.
2. Sum the digits within each chunk and convert the sum to a string.
3. Concatenate these string sums to update `s` for the next round.

### Complexity Analysis
* **Time Complexity:** \(\mathcal{O}(n)\) — The string length reduces each round, keeping total operations linear.
* **Space Complexity:** \(\mathcal{O}(n)\) — Required to store intermediate group representations and newly formed strings.

---

## 💻 Code Implementation

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_round = []
            for i in range(0, len(s), k):
                group_sum = sum(int(digit) for digit in s[i:i + k])
                next_round.append(str(group_sum))
            s = "".join(next_round)
        return s
```
