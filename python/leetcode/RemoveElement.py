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
    
# tested

# runtime 39ms - beats 71.55% of users
# memory 16.29mb - beats 44.09% of users


# refactored ver.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n, i in enumerate(nums):
            if i != val:
                nums[k] = i
                k += 1
        return k
    

# runtime 42ms - beats 48.46% of users
# memory 16.15mb - beats 76.06% of users

# negligible changes ..