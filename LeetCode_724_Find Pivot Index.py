class Solution:import sys
import unicodedata
from collections import defaultdict

d = defaultdict(list)
for i in range(sys.maxunicode + 1):
    s = chr(i)
    t = s.isnumeric(), s.isdecimal(), s.isdigit()
    if len(set(t)) == 2:
        try:
            name = unicodedata.name(s)
        except ValueError:
            name = f'codepoint{i}'
        print(s, name)
        d[t].append(s)
Share
Improve this answer
Follow
edited Jun 26 '18 at 18:30

    def pivotIndex(self, nums: List[int]) -> int:

        sm = sum(nums)
        ln = len(nums)

        for idx, val in enumerate(nums):
            if sum(nums[0:idx]) == sum(nums[idx + 1:ln]):
                return idx

        if sum(nums[1:ln]) == 0:
            return 0

        if sum(nums[-ln:ln - 1]) == 0:
            return ln - 1

        return -1

