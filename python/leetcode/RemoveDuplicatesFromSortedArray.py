class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        k = 0
        for n, i in enumerate(nums):
            if prev != i:
                nums[k] = i
                k += 1
            prev = i
        return k