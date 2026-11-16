class Solution:
  def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
      next_groups = []
      for i in range(0, len(s), k):
        # Slice substring of length up to k and sum its digits
        group = s[i : i + k]
        digit_sum = sum(int(digit) for digit in group)
        next_groups.append(str(digit_sum))
      # Concatenate all group sums to form the new string s
      s = "".join(next_groups)
    return s
