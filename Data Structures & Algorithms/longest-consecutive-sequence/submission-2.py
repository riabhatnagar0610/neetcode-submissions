class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        count = 1
        ans = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: continue
            if nums[i] == nums[i-1] + 1: 
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans