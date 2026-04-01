class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        n = len(nums)
        for i in range(0, n-k+1):
            currmax = -1
            for j in range(i, i+k):
                currmax = max(currmax, nums[j])
            output += [currmax]
        return output

        