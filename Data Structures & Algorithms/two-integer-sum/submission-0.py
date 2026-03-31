class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numsmap:
                return [numsmap[difference], i]
            numsmap[num] = i