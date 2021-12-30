class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        from collections import defaultdict
        d = defaultdict(int)
        ln = len(nums2)
        res = []

        d = defaultdict(lambda: -1, d)

        for idx, val in enumerate(nums2):
            for k in range(idx + 1, ln):
                if nums2[k] > val:
                    d[val] = nums2[k]
                    break

            # if d[val] == 0:
            #       d[val] = -1
        print(d)
        for i in nums1:
            res.append(d[i])
        return res
