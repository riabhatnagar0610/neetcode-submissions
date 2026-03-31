class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        for i in range(n):
            res = set()
            for j in range(i+1, n):
                complement = 0 - nums[i] - nums[j]
                if complement in res:
                    curr = tuple(sorted([nums[i], nums[j], complement]))
                    ans.add(curr)
                res.add(nums[j])
            
        return list(ans)     