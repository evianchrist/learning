class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n, i in enumerate(nums):
            if i == val:
                nums[n] = -1
            else:
                nums[k] = i
                k += 1
        return k