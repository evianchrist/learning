class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums)/2

        for i in nums:
            if nums.count(i) > x:
                return i