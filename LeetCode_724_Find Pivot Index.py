class Solution:
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

