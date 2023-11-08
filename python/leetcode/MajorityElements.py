class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums)/2
        rubbish = list()

        for i in nums:
            if not i in rubbish:
                if nums.count(i) > x:
                    return i
                else:
                    rubbish.append(i)