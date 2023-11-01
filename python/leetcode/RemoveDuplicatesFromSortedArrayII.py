class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0
        dup = 0
        for n, i in enumerate(nums):
            if dup == 0 or prev != i:
                nums[k] = i
                k += 1
            if i == prev:
                dup = 1
            else:
                dup = 0
            prev = i
        return k